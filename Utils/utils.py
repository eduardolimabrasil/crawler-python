import requests
from bs4 import BeautifulSoup
from settings import HEADERS


def request_soup(url):
    req = requests.get(url, headers=HEADERS)
    return BeautifulSoup(req.content, "lxml")

def save_file(name_file, text):
    with open(name_file , 'w') as file:
        file.write(text)