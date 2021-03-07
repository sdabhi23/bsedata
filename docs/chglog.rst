Change Log
==========

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
