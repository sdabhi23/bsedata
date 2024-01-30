"""

    MIT License

    Copyright (c) 2018 - 2024 Shrey Dabhi

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
    Class which implements the functionality for
    Bombay Stock Exchange (BSE)
    """

    def __init__(self, update_codes=False):
        self.__update_codes = update_codes
        if update_codes:
            self.updateScripCodes()

    def topGainers(self):
        """
        :returns: A sorted list of codes of top gainers
        """
        return gainers.getGainers()

    def topLosers(self):
        """
        :returns: A sorted list of codes of top losers
        """
        return losers.getLosers()

    def getQuote(self, scripCode):
        """
        :param scripCode: A stock code
        :returns: A dictionary which contain details about the stock
        :raises InvalidStockException: Raised for stocks which have been suspended or no longer trading on BSE
        """
        return quote.quote(scripCode)

    def getIndices(self, category):
        """
        :param category: A category of indices
        :returns: A dictionary with details about the indices belonging to the given category
        """
        return indices.indices(category)

    def updateScripCodes(self):
        """
        Download a fresh copy of the scrip code listing

        :returns: None
        """
        r = requests.get("https://pub-87b187a07d9c42109c9e6999439a583f.r2.dev/stk.json")
        f_stk = open("stk.json", "w+")
        f_stk.write(json.dumps(r.json()))
        f_stk.close()
        return

    def getScripCodes(self):
        """
        :returns: A dictionary with scrip codes as keys and company names as values
        """
        f = open("stk.json", "r")
        return json.loads(f.read())

    def verifyScripCode(self, code):
        """
        :returns: Company name if it is a valid stock code, else None
        """
        data = self.getScripCodes()
        return data.get(code)

    def __str__(self):
        return "Driver Class for Bombay Stock Exchange (BSE)"

    def __repr__(self):
        return f"<{self.__class__.__name__}: update_codes={self.__update_codes}> Driver Class for Bombay Stock Exchange (BSE)"
