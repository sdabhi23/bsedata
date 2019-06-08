"""

    MIT License

    Copyright (c) 2018 Shrey Dabhi

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

"""

from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint


def getGainers():
    baseurl = '''https://m.bseindia.com'''
    res = requests.get(baseurl)
    c = res.content
    soup = bs(c, "html.parser")
    for tag in soup("div"):
        try:
            if(tag['id'] == 'divGainers'):
                resSoup = tag
                break
        except KeyError:
            continue
    children = list(resSoup.table.contents)
    children = children[1:]
    gainers = []
    for tr in children:
        td = tr.contents
        gainer = {"securityID": str(td[0].a.string), "scripCode": str(tr.td.a["href"].split("=")[1]), "LTP": str(td[1].string), "change": str(td[2].string), "pChange": str(td[3].string)}
        gainers.append(gainer)
    return gainers
