from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def make_italic(func):
    def wrapper():
        return f'<em>{func()}</em'
    return wrapper

def make_underline(func):
    def wrapper():
        return f'<u>{func()}</u>'
    return wrapper



@app.route("/")
@make_bold
@make_italic
@make_underline
def hello_world():
    return "Hello, World !!"

@app.route("/bye")
def say_bye():
    return '<h1 style="text-align: center">Bye</h1>' \
    '<p>this is a paragraph</p>' \
    '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHF5dmliaW5uaHgyd241ZWx2N3ozbWh6dXZmMXVqaTlxNHNlbGN6cyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/eSwGh3YK54JKU/giphy.gif" width=200>'

@app.route("/<name>/<int:number>")
def greet(name,number):
    return f"hello {name} you are {number} old"

if __name__=="__main__":
    app.run(debug=True)