Introduction
============

.. image:: https://img.shields.io/pypi/v/bsedata.svg
   :target: https://pypi.org/project/bsedata/

.. image:: https://img.shields.io/pypi/l/bsedata.svg
   :target: https://pypi.org/project/bsedata/

.. image:: https://img.shields.io/pypi/pyversions/bsedata.svg
   :target: https://pypi.org/project/bsedata/

.. image:: https://img.shields.io/pypi/format/bsedata.svg
   :target: https://pypi.org/project/bsedata/

bsedata is a library for collecting real-time data from Bombay Stock Exchange (India). It can be used in various types of projects which require getting live quotes for a given stock or index or build large data sets for data analysis.

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - Tests (``master`` branch)
     - Tests (``dev`` branch)
     - Code coverage
     - Documentation
   * - |testsMaster|
     - |testsDev|
     - |codecovBadge|
     - |docBadge|

.. |docBadge| image:: https://readthedocs.org/projects/bsedata/badge/?version=latest
   :target: https://bsedata.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. |codecovBadge| image:: https://codecov.io/gh/sdabhi23/bsedata/branch/master/graph/badge.svg?token=QI8ZPA6ODL
   :target: https://codecov.io/gh/sdabhi23/bsedata
   :alt: Code Coverage

.. |testsMaster| image:: https://github.com/sdabhi23/bsedata/actions/workflows/tests.yml/badge.svg?branch=master
   :target: https://github.com/sdabhi23/bsedata/actions/workflows/tests.yml
   :alt: Status of tests on master branch

.. |testsDev| image:: https://github.com/sdabhi23/bsedata/actions/workflows/tests.yml/badge.svg?branch=dev
   :target: https://github.com/sdabhi23/bsedata/actions/workflows/tests.yml
   :alt: Status of tests on dev branch

.. note::

   The data provided by APIs is only as correct as provided on https://m.bseindia.com

.. warning::

   If you are facing any issue with the APIs then it may be beacuse there had been some format change recently in the way BSE reports its live quotes. Please upgrade to the latest version in order to avoid this issue. Report the issue at https://github.com/sdabhi23/bsedata/issues if it is not resolved even after upgrading the version.

Features
--------

* Live quotes using stock codes traded in BSE
* List of top losers
* List of top gainers
* Quotes for all the indices traded in BSE
* Helper APIs to check whether a given stock code or index code is correct
* List of all indices and stocks

Roadmap
-------

* Get details of an individual index
* Complete unit test coverage
* Daily OHLCV data
* Historical EOD OHLCV data

Dependencies
------------

* BeautifulSoup 4
* requests
* lxml
* A working internet connection 😉

.. warning::

   You need to have a working internet connection while using this library. It will raise ``requests.exceptions.ConnectionError`` in case there is no internet connectivity. Hence please handle this scenario in your code.
