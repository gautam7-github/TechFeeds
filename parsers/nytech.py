import requests
import xmltodict

URL = "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"


def parse():
    resp = requests.get(URL)

    tree = xmltodict.parse(resp.content)

    htmls = []
    for item in tree['rss']['channel']['item']:
        htmls.append(item)

    return htmls
