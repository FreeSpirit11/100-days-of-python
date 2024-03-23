from flask import Flask, render_template, request
import requests
import smtplib

my_email="my697253@gmail.com"
password="xxfrwtezcpgvqgls"

response = requests.get('https://api.npoint.io/1d97189a284dedec0b2a')
response.raise_for_status()
all_blogs = response.json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", blog_posts = all_blogs)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route('/post/<int:id>')
def post(id):
    requested_post = None
    for post in all_blogs:
        if post['id'] == id:
            requested_post = post
    return render_template("post.html", post = requested_post)

def send_email(name,email,phone,msg):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        message = f'Subject: new message \n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {msg}'
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=message)

if __name__ == "__main__":
    app.run(debug=True)