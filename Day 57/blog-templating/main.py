from flask import Flask, render_template
import requests
from Post import Post

app = Flask(__name__)
blog_url="https://api.npoint.io/c790b4d5cab58020d391"
response=requests.get(blog_url)
all_posts=response.json()

@app.route('/')
def home():
    return render_template("index.html",posts=all_posts)

@app.route("/post/<int:num>")
def post(num):
    # find post by numeric id (returns None if not found)
    this_post = Post(all_posts,num)
    f_post=this_post.get()
    return render_template("post.html",posts=f_post)

if __name__ == "__main__":
    app.run(debug=True)
