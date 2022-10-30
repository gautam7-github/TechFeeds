import requests
import xmltodict

URL = "https://techcrunch.com/feed/"


def parse():
    resp = requests.get(URL)

    tree = xmltodict.parse(resp.content)

    htmls = []
    for item in tree['rss']['channel']['item']:
        htmls.append(item)

    return htmls
