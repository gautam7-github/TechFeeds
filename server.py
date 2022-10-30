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
    vergeContent = verge.parse()
    techcrunchContent = techcrunch.parse()
    wiredContent = wired.parse()


@app.route("/technology", methods=["GET"])
def techfeed():
    return render_template(
        "techfeed.html",
        vergeContent=vergeContent,
        techcrunchContent=techcrunchContent,
        wiredContent=wiredContent
    )


if __name__ == "__main__":
    app.run(debug=True)
