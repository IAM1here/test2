from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Subdomain  Takeover POC by iam1here"
    return "The Subdomain is owned by microsoft and also this is just for demonstration"
