import time
import re
import wget

import requests

path = 'http://data.gdeltproject.org/events/'
url = 'http://data.gdeltproject.org/events/index.html'


def download():
    html = requests.get(url)
    #  Because bs4 crashed (max rec while parsing)
    links = re.findall('([0-9]+\.export.CSV.zip)', html.content)
    links = set(links)

    for i in links:
        print('processing {}'.format(i))
        link = ''.join([path, i])
        wget.download(link)
        time.sleep(10)  # be almost nice o_0


if __name__ == '__main__':
    download()
