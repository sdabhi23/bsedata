# bsedata

[![PyPi Version](https://img.shields.io/pypi/v/bsedata.svg)](https://pypi.org/project/bsedata/)
[![PyPi License](https://img.shields.io/pypi/l/bsedata.svg)](https://pypi.org/project/bsedata/)
[![PyPi PyVersions](https://img.shields.io/pypi/pyversions/bsedata.svg)](https://pypi.org/project/bsedata/)
[![PyPi Format](https://img.shields.io/pypi/format/bsedata.svg)](https://pypi.org/project/bsedata/)

Python library for extracting real-time data from Bombay Stock Exchange (India).

## Introduction

bsedata is a library for collecting real-time data from Bombay Stock Exchange (India). It can be used in various types of projects which require getting live quotes for a given stock or index or build large data sets for data analysis. You can also build CLI applications which can provide live market details at blazing fast speeds, much faster than that in a browser. The data is as accurate as provided on the [BSE website](m.bseindia.com).

## Roadmap:

- [x] Getting live quotes using stock codes.
- [x] Return data in both json and python (dict and list) formats.
- [x] Getting list of top losers.
- [x] Getting list of top gainers.
- [x] Getting quotes for all the indices traded in BSE.
- [ ] Adding function to fetch details of an individual index.
- [ ] Helper APIs to check whether a given stock code or index code is correct.
- [ ] Getting list of all indices and stocks.
- [ ] Cent percent unittest coverage.

## Dependencies

 * [BeautifulSoup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
 * [Requests](http://docs.python-requests.org/en/master/)
 * A working internet connection :wink:

## Usage

 * Installation using pip
    ```bash
    pip install bsedata
    ```
 * Instantiation
    ```python
    >>> from bsedata.bse import BSE
    >>> b = BSE()
    >>> print b
    Driver Class for Bombay Stock Exchange (BSE)
    ```
 * We will first see how to get a quote. Assume that we want to fetch current price of _**Infosys Technology**_. The only thing we need is BSE Scrip Code (Security Code) for this company. The BSE scrip code for Infosys is _500209_.
    ```python
    >>> q = b.getQuote("500209")
    >>> from pprint import pprint # just for neatness of display
    >>> pprint(q)
    {'2WeekAvgQuantity': '1.02 Lakh',
     '52weekHigh': '1290.50',
     '52weekLow': '861.50',
     'buy': {'1': {'price': '0.00', 'quantity': '-'},
             '2': {'price': '0.00', 'quantity': '-'},
             '3': {'price': '0.00', 'quantity': '-'},
             '4': {'price': '0.00', 'quantity': '-'},
             '5': {'price': '0.00', 'quantity': '-'}},
     'change': '5.55',
     'currentValue': '1277.85',
     'dayHigh': '1283.80',
     'dayLow': '1260.00',
     'faceValue': '5.00',
     'group': 'A  / S&P BSE SENSEX',
     'industry': 'IT Consulting & Software',
     'lowerPriceBand': '1145.10',
     'marketCapFreeFloat': '2,42,815.85 Cr.',
     'marketCapFull': '2,79,098.68 Cr.',
     'pChange': '0.44',
     'previousClose': '1272.30',
     'previousOpen': '1269.90',
     'priceBand': '10%',
     'scripCode': '500209',
     'securityID': 'INFY',
     'sell': {'1': {'price': '0.00', 'quantity': '-'},
              '2': {'price': '0.00', 'quantity': '-'},
              '3': {'price': '0.00', 'quantity': '-'},
              '4': {'price': '0.00', 'quantity': '-'},
              '5': {'price': '0.00', 'quantity': '-'}},
     'totalTradedQuantity': '0.77 Lakh',
     'totalTradedValue': '9.84 Cr.',
     'updatedOn': '26 Jun 18 | 04:00 PM',
     'upperPriceBand': '1399.50',
     'weightedAvgPrice': '1278.19'}
    ```
 * Top Gainers
    ```python
    >>> gainers = b.topGainers()
    >>> pprint(gainers)
    [{'LTP': '604.95',
      'change': '83.90',
      'pChange': '16.10',
      'scripCode': '512573',
      'securityID': 'AVANTI'},
     {'LTP': '278.45',
      'change': '20.00',
      'pChange': '7.74',
      'scripCode': '533274',
      'securityID': 'PRESTIGE'},
     {'LTP': '462.70',
      'change': '23.10',
      'pChange': '5.25',
      'scripCode': '532129',
      'securityID': 'HEXAWARE'},
     {'LTP': '57.85',
      'change': '2.75',
      'pChange': '4.99',
      'scripCode': '511431',
      'securityID': 'VAKRANGEE'},
     {'LTP': '588.15',
      'change': '25.60',
      'pChange': '4.55',
      'scripCode': '500940',
      'securityID': 'FINOLEXIND'}]
    ```
 * Top Losers
    ```python
    >>> losers = b.topLosers()
    >>> pprint(losers)
    [{'LTP': '54.50',
      'change': '-3.70',
      'pChange': '-6.36',
      'scripCode': '500116',
      'securityID': 'IDBI'},
     {'LTP': '79.35',
      'change': '-4.90',
      'pChange': '-5.82',
      'scripCode': '532345',
      'securityID': 'GATI'},
     {'LTP': '209.05',
      'change': '-12.55',
      'pChange': '-5.66',
      'scripCode': '500003',
      'securityID': 'AEGISLOG'},
     {'LTP': '78.55',
      'change': '-4.40',
      'pChange': '-5.30',
      'scripCode': '500378',
      'securityID': 'JINDALSAW'},
     {'LTP': '542.10',
      'change': '-29.35',
      'pChange': '-5.14',
      'scripCode': '540064',
      'securityID': 'FRETAIL'}]
    ```
 * Indices

    **Indices are currently available only as a part of a category**
    ```python
    >>> category = "corporate"
    # Category can be one of the following:
    # market_cap/broad
    # sector_and_industry
    # thematics
    # strategy
    # sustainability
    # volatility
    # composite
    # government
    # corporate
    # money_market
    >>> indices = d.getIndices(category)
    >>> pprint(indices)
    {'indices': [{'change': '0.00',
                  'currentValue': '149.02',
                  'name': 'S&P BSE India Corporate Bond Index',
                  'pChange': '0.00',
                  'scripFlag': 'SPBINCPT'},
                {'change': '0.00',
                  'currentValue': '148.74',
                  'name': 'S&P BSE India Financials Bond Index',
                  'pChange': '0.00',
                  'scripFlag': 'SPBINCFT'},
                {'change': '-0.32',
                  'currentValue': '153.82',
                  'name': 'S&P BSE India Services Bond Index',
                  'pChange': '-0.21',
                  'scripFlag': 'SPBINCST'},
                {'change': '+0.05',
                  'currentValue': '149.29',
                  'name': 'S&P BSE India Utilities Bond Index',
                  'pChange': '0.03',
                  'scripFlag': 'SPBINCUT'},
                {'change': '-0.01',
                  'currentValue': '153.59',
                  'name': 'S&P BSE India Industrials Bond Index',
                  'pChange': '0.00',
                  'scripFlag': 'SPBINCIT'}],
     'updatedOn': '27 Jul 2018'}
    ```

## License

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
