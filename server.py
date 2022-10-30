import requests
from flask import Flask, render_template

from parsers import techcrunch, verge, wired

app = Flask(__name__)

vergeContent = None
techcrunchContent = None
wiredContent = None


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.before_first_request
def runParsers():
    global vergeContent, techcrunchContent, wiredContent
    try:
        vergeContent = verge.parse()
        techcrunchContent = techcrunch.parse()
        wiredContent = wired.parse()
    except requests.exceptions.ConnectionError as e:
        print("Connection Error")
        print(e)


@app.route("/technology", methods=["GET"])
def techfeed():
    return render_template(
        "techfeed.html",
        vergeContent=vergeContent,
        techcrunchContent=techcrunchContent,
        wiredContent=wiredContent
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
