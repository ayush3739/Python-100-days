from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

API_URL = "https://api.perfecttense.com/correct"
USER_API_KEY = "696272ba1f7ebd07412b8644"
APP_KEY = "YOUR_APP_KEY"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    text = request.form.get("text", "")
    headers = {
        "Authorization": USER_API_KEY,
        "AppAuthorization": APP_KEY,
        "Content-Type": "application/json"
    }
    payload = { "text": text, "responseType": ["corrected"] }

    result = requests.post(API_URL, json=payload, headers=headers)
    return jsonify(result.json())

if __name__ == "__main__":
    app.run(debug=True)
