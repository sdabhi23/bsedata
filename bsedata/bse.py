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

from . import losers, gainers, quote, index
import requests
import json


class BSE:

    def topGainers(self):
        return gainers.getGainers()

    def topLosers(self):
        return losers.getLosers()

    def getQuote(self, scripCode):
        return quote.quote(scripCode)

    def getIndices(self, category):
        return index.indices(category)

    def updateScripCodes(self):
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
        f = open('stk.json', 'r')
        return json.loads(f.read())

    def verifyScripCode(self, code):
        data = self.getScripCodes()
        try:
            return data.get(code)
        except KeyError:
            return None

    def __str__(self):
        return 'Driver Class for Bombay Stock Exchange (BSE)'

    def __repr__(self):
        return 'Driver Class for Bombay Stock Exchange (BSE)'


# TODO: add unit tests
# TODO: add documentation
# TODO: getIndices()
# TODO: isMarketOpen()
# TODO: fetching some particular fields in bulk (for portfolios)
"""
HACK:
    You can use the following code to get details in bulk
    >>> b = BSE()
    >>> codelist = ["500116", "512573"]
    >>> for code in codelist
    ...     quote = b.quote(code)
    ...     pprint(quote.companyName)
    ...     pprint(quote.currentValue)
    ...     pprint(quote.updatedOn)
"""
