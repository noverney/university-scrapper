# get a browser to emulate 
# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.parse import urlparse
import os
import time

def get_items(page_source,url,tag):
    base_url = "https://"+urlparse(url, scheme="http").netloc
    # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(page_source, "html.parser")

    table = soup.find("div", {"class": "masonry-wrapper"})
    print("Found Table!")
    links = []
    for i,link in enumerate(table.find_all('a')):
        print("Found article:",i)
        fulllink = link.get ('href')
        links.append(urljoin(base_url,fulllink))
    soup.decompose()
    return links

def get_text(url):
    f = urllib.request.urlopen(url)
    soup = BeautifulSoup(f.read(), "html.parser")
    text = soup.find("div", {"class": "item-body"})
    soup.decompose()
    return text

if __name__ == "__main__":
    url = "https://markt.unibas.ch/article/studentenhaus-im-erlenmattquartier"
    print(get_text(url))