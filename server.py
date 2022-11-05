

import random

import requests
from flask import Flask, render_template

from parsers import techcrunch, verge, wired

app = Flask(__name__)

store = {
    'Verge': None,
    'Tech-Crunch': None,
    'Wired': None
}


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.before_first_request
def runParsers():
    global store
    try:
        vergeContent = verge.parse()
        techcrunchContent = techcrunch.parse()
        wiredContent = wired.parse()
        store['Tech-Crunch'] = techcrunchContent
        store['Verge'] = vergeContent
        store['Wired'] = wiredContent
    except requests.exceptions.ConnectionError as e:
        print("Connection Error")
        print(e)


@app.route("/technology", methods=['GET'])
def technology():
    # provider = choice(list(store.keys()))
    return render_template(
        "techfeed-home.html",
    )


@app.route("/technology/<provider>", methods=["GET"])
def techfeedforProvider(provider: str):
    # provider = provider.capitalize()
    if provider in store:
        return render_template(
            "techfeed.html",
            mainContent=store[provider],
            provider=provider
        )


@app.route("/technology/all", methods=["GET"])
def techfeedforAll():
    allProviders = list(store.values())
    allProviders = random.shuffle(allProviders)
    # print(allProviders)
    return render_template(
        "techfeed-all.html",
        mainContent=allProviders
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
