from flask import Flask, render_template

from parsers import verge

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    vergeContent = verge.parse()
    return render_template("index.html", vergeContent=vergeContent)


if __name__ == "__main__":
    app.run(debug=True)
