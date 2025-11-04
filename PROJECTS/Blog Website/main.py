from flask import Flask
from flask import render_template,request
import requests,smtplib,os
from dotenv import load_dotenv
load_dotenv('.env')

from_email=os.getenv('email')
to_email=os.getenv('to_email')
passw=os.getenv('pass')

app=Flask(__name__)

response=requests.get('https://api.npoint.io/a488fedba3cea47fdfa7')
response=response.json()


@app.route('/')
def home():
    return render_template("index.html",all_posts=response)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        send_mail(data["name"],data["email"],data["phone"],data["message"])
        
        return render_template("contact.html",msg_sent=True)
    return render_template("contact.html",msg_sent=False)

@app.route("/post/<int:index>")
def show_post(index):
    for post in response:
        if post['id']==index:
            requested_post=post
    return render_template("post.html",post=requested_post)

def send_mail(name, email, phone, message):
    email_msg=f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone No.: {phone}\nMessage: {message}"
    with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(from_email,passw)            
            connection.sendmail(from_addr=email,
                                to_addrs=to_email,
                                msg=email_msg)


if __name__=="__main__":
    app.run(debug=True)