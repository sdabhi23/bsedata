# bsedata

[![PyPi Version](https://img.shields.io/pypi/v/bsedata.svg)](https://pypi.org/project/bsedata/)
[![PyPi License](https://img.shields.io/pypi/l/bsedata.svg)](https://pypi.org/project/bsedata/)
[![PyPi PyVersions](https://img.shields.io/pypi/pyversions/bsedata.svg)](https://pypi.org/project/bsedata/)
[![PyPi Format](https://img.shields.io/pypi/format/bsedata.svg)](https://pypi.org/project/bsedata/)

Python library for extracting real-time data from Bombay Stock Exchange (India).

| Tests on `master` branch                  | Tests on `dev` branch               | Code coverage                                 | Documentation                         |
| ----------------------------------------- | ----------------------------------- | --------------------------------------------- | ------------------------------------- |
| [![tests master][testsmaster]][testslink] | [![tests dev][testsdev]][testslink] | [![code coverage][codecovbadge]][codecovlink] | [![documentation][docbadge]][doclink] |

[testsmaster]: https://github.com/sdabhi23/bsedata/actions/workflows/tests.yml/badge.svg?branch=master
[testsdev]: https://github.com/sdabhi23/bsedata/actions/workflows/tests.yml/badge.svg?branch=dev
[testslink]: https://github.com/sdabhi23/bsedata/actions/workflows/tests.yml
[codecovbadge]: https://codecov.io/gh/sdabhi23/bsedata/branch/master/graph/badge.svg?token=QI8ZPA6ODL
[codecovlink]: https://codecov.io/gh/sdabhi23/bsedata
[docbadge]: https://readthedocs.org/projects/bsedata/badge/?version=latest
[doclink]: https://bsedata.readthedocs.io/en/latest/?badge=latest

## Introduction

bsedata is a library for collecting real-time data from Bombay Stock Exchange (India). It can be used in various types of projects which require getting live quotes for a given stock or index or build large data sets for data analysis.

The data is as accurate as provided on the [BSE website](m.bseindia.com).

> **Please do not use this application for production usage. It is best used for learning and building application for your own use. For commercial application you better buy a data service.**
>
> **This library uses MIT license hence liability lies with the user and not the author of the application.**
>
> **As per India's IT act it is no where mentioned that we cannot scrape a website. It's up to me whether I consume the publicly available data "visually" or through my programme or using some kind of "web reader". As long as data you are scrapping is available in public domain and you are not breaching security and accessing data of private nature with malicious intent, it cannot be termed as illegal.**
>
> **But it can certainly be termed "unethical" (which is equally bad) since you are damaging the service itself. Hence be prudent about how much stress you cause to the backend. BSE's website is very capable and even they will not mind if someone is scrapping their website for educational purposes.**

## Features

- Getting live quotes using stock codes in Python dicttionaries
- Getting list of top losers
- Getting list of top gainers
- Getting quotes for all the indices traded in BSE
- Helper APIs to check whether a given stock code or index code is correct
- Getting list of all indices and stocks

## Roadmap

- Get details of an individual index
- Complete unit test coverage
- Daily OHLCV data

## Dependencies

- [BeautifulSoup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests](http://docs.python-requests.org/en/master/)
- [lxml](https://lxml.de/)
- A working internet connection :wink:

## Usage

Refer the documentation at <https://bsedata.readthedocs.io/en/latest/usage.html>

## Change Log

Refer the documentation at <https://bsedata.readthedocs.io/en/latest/chglog.html>

## License

MIT License

Copyright (c) 2018 - 2023 Shrey Dabhi

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
