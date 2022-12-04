import requests
import xmltodict

URL = "https://feeds.howtogeek.com/HowToGeek"


def parse():
    resp = requests.get(URL)

    tree = xmltodict.parse(resp.content)

    htmls = []
    for item in tree['rss']['channel']['item']:
        htmls.append(item)

    return htmls
