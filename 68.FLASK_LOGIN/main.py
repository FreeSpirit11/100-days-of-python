from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

# Configure Flask-Login's Login Manager
login_manager = LoginManager()
login_manager.init_app(app)


# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get('email')
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        if user:
            # User already exists
            flash("You have already signed up with that email.Log in instead.")
            return redirect(url_for("login"))

        hash_and_salted_password = generate_password_hash(request.form['password'], method='pbkdf2:sha256', salt_length=8)
        # Storing the hashed password in our database
        new_user = User(
            name=request.form['name'],
            email=request.form['email'],
            password=hash_and_salted_password
        )
        db.session.add(new_user)
        db.session.commit()

        # Log in and authenticate user after adding details to database.

        login_user(new_user)
        return redirect(url_for("secrets"))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        # Find user by email entered.
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        # Email doesn't exist or password incorrect.

        if not user:
            flash("That email does not exist.Please try again.")
            return redirect(url_for("login"))
        # Check stored password hash against entered password hashed.
        elif not check_password_hash(user.password, password):
            flash("Incorrect Password.Please try again.")
        #You can redirect to another template too then redirect to login to flash messages but once you have displayed
        #The messages are cleared from the session once they are retrieved using get_flashed_messages,
        # so they won't be   displayed again on subsequent requests.
            return redirect(url_for("login"))
        else:
            login_user(user)
            return redirect(url_for('secrets'))

    return render_template("login.html", logged_in=current_user.is_authenticated)
#You can just edit 'index.html' ,'base.html' file like this, and it will give you the same result.
#{% if not current_user.is_authenticated: %}

# Only logged-in users can access the route
@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", name=current_user.name, logged_in=True)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


# Only logged-in users can down download the pdf
@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
