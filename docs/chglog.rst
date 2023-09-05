Change Log
==========

v0.5.4
------

**Breaking Changes:**

- Drop the ``getPeriodTrend`` function due to increased security on the new BSE api


v0.5.3
------

**Bug Fixes:**

- Quick fix for ``getQuote`` method crashing due to missing ``priceBand`` attribute and missing error text on the website [:issue:`14`, :issue:`31`, :issue:`36`]

**Breaking Changes:**

- Python < 3.7 is no longer officially supported, i.e. the library has not been tested on those Python version in CI. However, it may still continue to work on those versions

v0.5.2
------

**Bug Fixes:**

- Fix the issue where the ``getIndices`` function would return an empty list without erroring out and add tests to catch it [:issue:`12`]

v0.5.1
------

**Bug Fixes:**

- Update the Quandl scrip code file link [:issue:`33`, :issue:`32`]

**Misc:**

- Drop CI for Python 3.6
- Add cron for tests to catch issues early

v0.5.0
------

**Breaking Changes:**

- Python < 3.6 is no longer officially supported, i.e. the library has not been tested on those Python version in CI. However, it may still continue to work on those versions

**New Features:**

- Get historic price trend of a stock over certain fixed time intervals (``1M``, ``3M``, ``6M``, ``12M``)
- Add custom exception for invalid or inactive stocks whose data is not available anymore [:issue:`2`, :issue:`18`, :issue:`22`]

**Misc:**

- Remove Travis piplines. This project now uses only GitHub Actions for CI!
- Add code coverage details to CI
- Update docs theme

v0.4.0
------

**New Features:**

- Switched to lxml parser for better performance

**Bug Fixes:**

- Add a generic User Agent to all the requests as BSE website is blocking requests from the default requests user agent (``python-requests/2.23.0``) [:issue:`5`, :issue:`9`, :issue:`13`, :issue:`14`]

v0.3.1
------

**Bug Fixes:**

- Quick fix for getQuote method crashing due to missing ``priceBand`` attribute [:issue:`5`]

v0.3.0
------

**New Features:**

- Implement ``updateScripCodes``, ``getScripCodes`` and ``verifyScripCode`` methods to verify and search scrip codes

**Bug Fixes:**

- Fix ``getIndices`` method returning empty response
- Fix ``getQuote`` method not returning company name


v0.2.0
------

**New Features:**

- Getting quotes for all the indices traded in BSE

v0.1.0
------

**New Features:**

- Getting live quotes using stock codes
- Return data in both JSON and python (dict and list) formats
- Getting list of top losers
- Getting list of top gainers
