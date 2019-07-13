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

from . import losers, gainers, quote, indices
import requests
import json


class BSE(object):
    """
    class which implements all the functionality for
    National Stock Exchange
    """

    def __init__(self, update_codes = False):

        if update_codes:
            self.updateScripCodes()

    def topGainers(self):
        """
        :return: a sorted list of codes of top gainers
        """
        return gainers.getGainers()

    def topLosers(self):
        """
        :return: a sorted list of codes of top losers
        """
        return losers.getLosers()

    def getQuote(self, scripCode):
        """
        :param scripCode: a stock code
        :return: a dictionary which contain details about the stock
        """
        return quote.quote(scripCode)

    def getIndices(self, category):
        """
        :param category: a category of indices
        :return: a dictionary with details about the indices belonging to the given category
        """
        return indices.indices(category)

    def updateScripCodes(self):
        """
        Download a fresh copy of the scrip code listing
        :return: None
        """
        r = requests.get('https://s3.amazonaws.com/quandl-static-content/BSE%20Descriptions/stocks.txt')
        stk = {x.split("|")[1][3:]: x.split("|")[0][:-11] for x in r.text.split("\n") if x != '' and x.split("|")[1][:3] == 'BOM'}
        stk.pop("CODE", None)
        indices = {x.split("|")[1]: x.split("|")[0] for x in r.text.split("\n") if x != '' and x.split("|")[1][:3] != 'BOM'}
        indices.pop("CODE", None)
        f_stk = open('stk.json', 'w+')
        f_stk.write(json.dumps(stk))
        f_stk.close()
        f_indices = open('indices.json', 'w+')
        f_indices.write(json.dumps(indices))
        f_indices.close()
        return

    def getScripCodes(self):
        """
        :return: a dictionary with scrip codes as keys and company names as values
        """
        f = open('stk.json', 'r')
        return json.loads(f.read())

    def verifyScripCode(self, code):
        """
        :return: company name if it is a valid stock code, else None
        """
        data = self.getScripCodes()
        try:
            return data.get(code)
        except KeyError:
            return None

    def __str__(self):
        return 'Driver Class for Bombay Stock Exchange (BSE)'

    def __repr__(self):
        return 'Driver Class for Bombay Stock Exchange (BSE)'
