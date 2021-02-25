from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Subdomain  Takeover POC by hackerone.com/rootmatters"
