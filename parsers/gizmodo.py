import requests
import xmltodict

URL = "https://gizmodo.com/rss"


def parse():
    resp = requests.get(URL)

    tree = xmltodict.parse(resp.content)

    htmls = []
    for item in tree['rss']['channel']['item']:
        htmls.append(item)

    return htmls
