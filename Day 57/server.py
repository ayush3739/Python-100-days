from flask import Flask
from flask import render_template
import random,requests
import datetime
current_year=datetime.datetime.now().year

# n_point docs="https://www.npoint.io/"
fake_blogs_npoint="https://www.npoint.io/docs/c790b4d5cab58020d391"
api_npoint="https://api.npoint.io/c790b4d5cab58020d391"


app=Flask(__name__)

@app.route('/')
def home():
    random_no=random.randint(1,10)
    return render_template("index.html",num=random_no,Year=current_year)

@app.route('/guess/<string:name>')
def agify(name):
    age=requests.get(f"https://api.agify.io?name={name}")
    guess_Age=age.json()["age"]
    gender=requests.get(f"https://api.genderize.io?name={name}")
    guess_gender=gender.json()["gender"]
    return render_template("Guessify.html",Person_name=name,age=guess_Age,gender=guess_gender)

@app.route("/blog")
def get_blog():
    blog_url="https://api.npoint.io/c790b4d5cab58020d391"
    response=requests.get(blog_url)
    all_posts=response.json()
    return render_template("blog.html",posts=all_posts)

if __name__=="__main__":
    app.run(debug=True)

