# -*- coding: UTF-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError



def getBsObj(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),features="html.parser")

    except AttributeError as e:
        return None
    return bsObj