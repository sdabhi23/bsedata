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

class BSE:

    def topGainers(self):
        return gainers.getGainers()

    def topLosers(self):
        return losers.getLosers()

    def getQuote(self, scripCode):
        return quote.quote(scripCode)

    def getIndices(self, category):
        return index.indices(category)

    def __str__(self):
        return 'Driver Class for Bombay Stock Exchange (BSE)'

    def __repr__(self):
        return 'Driver Class for Bombay Stock Exchange (BSE)'

# TODO: add unit tests
# TODO: add documentation
# TODO: getIndices()
# TODO: getScripCodes()
# TODO: verifyScripCode()
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
