from flask import Flask
import random

random_num=random.randint(0,9)

app=Flask(__name__)

@app.route('/')
def home():
    return '<h1> Guess a number from 0 to 9 in the url</h1>' \
    '<img src="https://i.giphy.com/3o7aCSPqXE5C6T8tBC.webp" width=400>'

@app.route("/<int:guess>")
def guess_number(guess):
    if guess>random_num:
        return '<h1 style="color:Red">Too High, Try again!</h1>' \
        '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    
    elif guess<random_num:
        return '<h1 style="color: Purple">Too Low, Try again!</h1>' \
        '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"'
    
    else:
        return '<h1 style="color:Green">You Found Me!</h1>' \
        '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>'
 

if __name__=="__main__":
    app.run(debug=True)
