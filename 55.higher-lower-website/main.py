from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a paragraph.</p>'
            '<img src="https://media.giphy.com/media/gyRWkLSQVqlPi/giphy.gif?cid=ecf05e47odx31h0ctpnuwk9dhg6r4ufahmilo9knb2f2l6ag&ep=v1_gifs_search&rid=giphy.gif&ct=g", width=600>')

def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper
def make_emphasis(func):
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper
def make_underlined(func):
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

@app.route("/<name>/<path:date>/<int:age>")
def greet(name,date,age):
    return f"Hello {name}! today's date is {date}, you are {age} years old. "


if __name__ == "__main__":
    app.run(debug=True)