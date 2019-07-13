# bsedata

[![PyPi Version](https://img.shields.io/pypi/v/bsedata.svg)](https://pypi.org/project/bsedata/)
[![PyPi License](https://img.shields.io/pypi/l/bsedata.svg)](https://pypi.org/project/bsedata/)
[![PyPi PyVersions](https://img.shields.io/pypi/pyversions/bsedata.svg)](https://pypi.org/project/bsedata/)
[![PyPi Format](https://img.shields.io/pypi/format/bsedata.svg)](https://pypi.org/project/bsedata/)

Python library for extracting real-time data from Bombay Stock Exchange (India).

## Introduction

bsedata is a library for collecting real-time data from Bombay Stock Exchange (India). It can be used in various types of projects which require getting live quotes for a given stock or index or build large data sets for data analysis.

The data is as accurate as provided on the [BSE website](m.bseindia.com).

## Features:

* Getting live quotes using stock codes in Python dicttionaries
* Getting list of top losers
* Getting list of top gainers
* Getting quotes for all the indices traded in BSE
* Helper APIs to check whether a given stock code or index code is correct
* Getting list of all indices and stocks

## Roadmap:

* Get details of an individual index
* Complete unit test coverage
* Daily OHLCV data
* Historical EOD OHLCV data

## Dependencies

* [BeautifulSoup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Requests](http://docs.python-requests.org/en/master/)
* A working internet connection :wink:

## Usage

Refer the documentation at https://bsedata.readthedocs.io/en/latest/usage.html

## Change Log



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
