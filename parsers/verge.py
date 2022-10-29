import requests
import xmltodict

URL = "https://www.theverge.com/rss/frontpage"


def parse():
    resp = requests.get(URL)

    tree = xmltodict.parse(resp.content)

    htmls = []
    for x in tree['feed']['entry']:
        htmls.append(x)

    return htmls
