Usage
=====

.. warning::

    Refrain from using this library if you are trying to query the stock exchange very very frequently.
    It increases load on BSE's servers and might even lead to your IP address being blacklisted by them.
    Apart from the technical issues, it's higly unethical.

    For frequent queries, consider buying data from BSE or a vendor. More details are available at https://www.bseindia.com/market_data_products.html

Installing with pip
-------------------

.. code-block:: Bash

    pip install bsedata

Instantiation
-------------

.. code-block:: Python

    from bsedata.bse import BSE
    b = BSE()
    print(b)
    # Output:
    # Driver Class for Bombay Stock Exchange (BSE)

    # to execute "updateScripCodes" on instantiation
    b = BSE(update_codes = True)

Getting a stock quote
---------------------

This method returns all the publicly available data, you can pick the fields you require from the dictionary

.. code-block:: Python

    q = b.getQuote('534976')
    pprint(q)
    # Output:
    # {'2WeekAvgQuantity': '0.14 Lakh',
    #  '52weekHigh': '3298.00',
    #  '52weekLow': '1874.00',
    #  'buy': {'1': {'price': '0.00', 'quantity': '-'},
    #          '2': {'price': '0.00', 'quantity': '-'},
    #          '3': {'price': '0.00', 'quantity': '-'},
    #          '4': {'price': '0.00', 'quantity': '-'},
    #          '5': {'price': '0.00', 'quantity': '-'}},
    #  'change': '76.75',
    #  'companyName': 'V-MART RETAIL LTD.',
    #  'currentValue': '2255.80',
    #  'dayHigh': '2270.00',
    #  'dayLow': '2185.10',
    #  'faceValue': '10.00',
    #  'group': 'A  / S&P BSE 500',
    #  'industry': 'Department Stores',
    #  'lowerPriceBand': '1804.65',
    #  'marketCapFreeFloat': '1,883.72 Cr.',
    #  'marketCapFull': '4,095.05 Cr.',
    #  'pChange': '3.52',
    #  'previousClose': '2179.05',
    #  'previousOpen': '2199.65',
    #  'priceBand': '20%',
    #  'scripCode': '534976',
    #  'securityID': 'VMART',
    #  'sell': {'1': {'price': '0.00', 'quantity': '-'},
    #           '2': {'price': '0.00', 'quantity': '-'},
    #           '3': {'price': '0.00', 'quantity': '-'},
    #           '4': {'price': '0.00', 'quantity': '-'},
    #           '5': {'price': '0.00', 'quantity': '-'}},
    #  'totalTradedQuantity': '0.01 Lakh',
    #  'totalTradedValue': '0.13 Cr.',
    #  'updatedOn': '14 Jun 19 | 04:00 PM',
    #  'upperPriceBand': '2706.95',
    #  'weightedAvgPrice': '2239.58'}

.. note::

    You can use the following code to get quotes in bulk

    .. code-block:: Python

        b = BSE()
        codelist = ["500116", "512573"]
        for code in codelist:
            quote = b.getQuote(code)
            pprint(quote["companyName"])
            pprint(quote["currentValue"])
            pprint(quote["updatedOn"])

Getting top gainers
-------------------

.. code-block:: Python

    tg = b.topGainers()
    pprint(tg)
    # Output:
    # [{'LTP': '2,255.80',
    #   'change': '76.75',
    #   'pChange': '3.52',
    #   'scripCode': '534976',
    #   'securityID': 'VMART'},
    #  {'LTP': '274.30',
    #   'change': '9.25',
    #   'pChange': '3.49',
    #   'scripCode': '538835',
    #   'securityID': 'INTELLECT'},
    #  {'LTP': '273.65',
    #   'change': '9.20',
    #   'pChange': '3.48',
    #   'scripCode': '500620',
    #   'securityID': 'GESHIP*'},
    #  {'LTP': '3,092.55',
    #   'change': '103.50',
    #   'pChange': '3.46',
    #   'scripCode': '539658',
    #   'securityID': 'TEAMLEASE'},
    #  {'LTP': '164.75',
    #   'change': '5.45',
    #   'pChange': '3.42',
    #   'scripCode': '532636',
    #   'securityID': 'IIFL'}]

Getting top losers
------------------

.. code-block:: Python

    tg = b.topLosers()
    pprint(tg)
    # Output:
    # [{'LTP': '82.05',
    #   'change': '-9.90',
    #   'pChange': '-10.77',
    #   'scripCode': '532617',
    #   'securityID': 'JETAIRWAYS'},
    #  {'LTP': '76.55',
    #   'change': '-7.85',
    #   'pChange': '-9.30',
    #   'scripCode': '500111',
    #   'securityID': 'RELCAPITAL'},
    #  {'LTP': '326.55',
    #   'change': '-26.40',
    #   'pChange': '-7.48',
    #   'scripCode': '539268',
    #   'securityID': 'SYNGENE'},
    #  {'LTP': '3.69',
    #   'change': '-0.29',
    #   'pChange': '-7.29',
    #   'scripCode': '532532',
    #   'securityID': 'JPASSOCIAT'},
    #  {'LTP': '57.40',
    #   'change': '-4.25',
    #   'pChange': '-6.89',
    #   'scripCode': '534809',
    #   'securityID': 'PCJEWELLER'}]


Getting Period Trend data
-------------------------

Get historic price trend of a stock over certain fixed period of time. This data can be used to visualize the trends in the stock price

.. note::

    The available period options are ``'1M'``, ``'3M'``, ``'6M'`` and ``'12M'``.

.. code-block:: Python

    his = b.getPeriodTrend('534976','6M')
    pprint(q)
    # Output:
    # [{'date': 'Tue Jan 12 2021 00:00:00', 'value': '2453.10', 'vol': '791'},
    #  {'date': 'Wed Jan 13 2021 00:00:00', 'value': '2422.15', 'vol': '771'},
    #  {'date': 'Thu Jan 14 2021 00:00:00', 'value': '2417.45', 'vol': '423'},
    #  {'date': 'Fri Jan 15 2021 00:00:00', 'value': '2404.45', 'vol': '228'},
    #  {'date': 'Mon Jan 18 2021 00:00:00', 'value': '2415.25', 'vol': '241'},
    #  {'date': 'Tue Jan 19 2021 00:00:00', 'value': '2437.10', 'vol': '589'},
    #  {'date': 'Wed Jan 20 2021 00:00:00', 'value': '2410.20', 'vol': '809'},
    #  {'date': 'Thu Jan 21 2021 00:00:00', 'value': '2473.40', 'vol': '4657'},
    #  {'date': 'Fri Jan 22 2021 00:00:00', 'value': '2495.10', 'vol': '1671'},
    #  {'date': 'Mon Jan 25 2021 00:00:00', 'value': '2496.25', 'vol': '636'},
    #  {'date': 'Wed Jan 27 2021 00:00:00', 'value': '2399.90', 'vol': '1063'},
    #  {'date': 'Thu Jan 28 2021 00:00:00', 'value': '2417.30', 'vol': '3635'},
    #  {'date': 'Fri Jan 29 2021 00:00:00', 'value': '2453.15', 'vol': '129'},
    #  {'date': 'Mon Feb 01 2021 00:00:00', 'value': '2457.35', 'vol': '785'},
    #  {'date': 'Tue Feb 02 2021 00:00:00', 'value': '2451.95', 'vol': '176'},
    #  {'date': 'Wed Feb 03 2021 00:00:00', 'value': '2458.30', 'vol': '1689'},
    #  {'date': 'Thu Feb 04 2021 00:00:00', 'value': '2493.30', 'vol': '1433'},
    #  {'date': 'Fri Feb 05 2021 00:00:00', 'value': '2478.40', 'vol': '1066'},
    #  {'date': 'Mon Feb 08 2021 00:00:00', 'value': '2472.95', 'vol': '1037'},
    #  {'date': 'Tue Feb 09 2021 00:00:00', 'value': '2446.55', 'vol': '1013'},
    #  {'date': 'Wed Feb 10 2021 00:00:00', 'value': '2485.20', 'vol': '313'},
    #  {'date': 'Thu Feb 11 2021 00:00:00', 'value': '2982.20', 'vol': '16605'},
    #  {'date': 'Fri Feb 12 2021 00:00:00', 'value': '2881.35', 'vol': '8452'}]

Getting indices
---------------

.. note::

    Indices are currently available only as a part of a category

``category`` parameter can be one of the following:

#. market_cap/broad
#. sector_and_industry
#. thematics
#. strategy
#. sustainability
#. volatility
#. composite
#. government
#. corporate
#. money_market

.. code-block:: Python

    indices = b.getIndices(category='corporate')
    pprint(indices)
    # Output:
    # {'indices': [{'change': '-0.31',
    #               'currentValue': '162.58',
    #               'name': 'S&P BSE India Corporate Bond Index',
    #               'pChange': '-0.19',
    #               'scripFlag': 'SPBINCPT'},
    #              {'change': '-0.40',
    #               'currentValue': '162.63',
    #               'name': 'S&P BSE India Financials Bond Index',
    #               'pChange': '-0.25',
    #               'scripFlag': 'SPBINCFT'},
    #              {'change': '+0.05',
    #               'currentValue': '169.10',
    #               'name': 'S&P BSE India Services Bond Index',
    #               'pChange': '0.03',
    #               'scripFlag': 'SPBINCST'},
    #              {'change': '+0.40',
    #               'currentValue': '165.34',
    #               'name': 'S&P BSE India Utilities Bond Index',
    #               'pChange': '0.24',
    #               'scripFlag': 'SPBINCUT'},
    #              {'change': '+0.09',
    #               'currentValue': '162.87',
    #               'name': 'S&P BSE India Industrials Bond Index',
    #               'pChange': '0.05',
    #               'scripFlag': 'SPBINCIT'}],
    #  'updatedOn': '13 Jun 2019'}

Updating list of scrip codes
----------------------------

Downloads a fresh list of scrip codes from publicly available Quandl data and resfreshes the library cache.

.. code-block:: Python

    b.updateScripCodes()
    # returns nothing

Verifying a scrip code
----------------------

Verify if a scrip code is valid or not

.. code-block:: Python

    b.updateScripCodes()

    # Valid scrip code

    pprint(b.verifyScripCode('534976'))
    # Output:
    # V-mart Retail Ltd.

    # invalid scrip code

    pprint(b.verifyScripCode('534980'))
    # Output:
    # None

Getting all listed companies and their scrip codes
--------------------------------------------------

.. code-block:: Python

    pprint(b.getScripCodes())
    # Output too large to display in docs
    # returns a dictionary with scrip codes as keys and respective company names as values