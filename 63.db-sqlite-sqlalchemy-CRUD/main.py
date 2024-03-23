from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Book-collection.db"
db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


@app.route('/')
def home():
    result = db.session.execute(db.select(Book))
    all_books = result.scalars().all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['POST','GET'])
def add():
    if request.method == 'POST':
        book = Book(title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit', methods=['GET','POST'])
def edit():
    id = request.args.get('id')
    book_selected = db.get_or_404(Book, id)
    if request.method == 'POST':
        book_selected.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', book=book_selected)

@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

'''
in edit.html 
         <input hidden="hidden" name="id" value="{{book.id}}">
in main.py
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        
this angela yu did but there is no requirement of it . i have just added 
this here for knowledge that we can create hidden inputs.
'''

'''
also you can do '/edit/<id>' in route, just pass id in index.html and form.html edit url.
but it will give the url as this then http://127.0.0.1:5000/edit/1
currently it is like this http://127.0.0.1:5000/edit?id=1
'''