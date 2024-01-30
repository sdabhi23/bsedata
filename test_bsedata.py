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

import time
import pytest
import datetime
from bsedata.bse import BSE
from bsedata.exceptions import InvalidStockException, BhavCopyNotFound

b = BSE(update_codes=True)


def test_str():
    assert str(b) == "Driver Class for Bombay Stock Exchange (BSE)"


def test_repr():
    assert (
        repr(b)
        == "<BSE: update_codes=True> Driver Class for Bombay Stock Exchange (BSE)"
    )


@pytest.mark.parametrize("scripCode", ["534976", "500116", "512573"])
def test_getQuote_valid(scripCode):
    data = b.getQuote(scripCode)
    if "priceBand" not in data.keys():
        assert len(data) == 24
    else:
        assert len(data) == 27


def test_getQuote_invalid_default():
    with pytest.raises(InvalidStockException) as err_info:
        b.getQuote("513715")

    assert err_info.value.status == "Inactive stock"


def test_getQuote_invalid_custom():
    with pytest.raises(InvalidStockException) as err_info:
        b.getQuote("538936")

    assert err_info.value.status == "Suspended due to Procedural reasons"


@pytest.mark.parametrize(
    "scrip_code,scrip_name",
    [
        ("534976", "V-MART RETAIL LTD."),
        ("542649", "Rail Vikas Nigam Ltd"),
        ("541557", "Fine Organic Industries Ltd"),
    ],
)
def test_verifyCode_valid(scrip_code, scrip_name):
    assert b.verifyScripCode(scrip_code) == scrip_name


def test_verifyCode_invalid():
    assert b.verifyScripCode("534980") == None


@pytest.mark.parametrize(
    "category",
    [
        "market_cap/broad",
        "sector_and_industry",
        "thematics",
        "strategy",
        "sustainability",
        "volatility",
        "composite",
        "government",
        "corporate",
        "money_market",
    ],
)
def test_getIndices(category):
    indices = b.getIndices(category)
    datetime.datetime.strptime(indices["updatedOn"], "%d %b %Y")
    assert len(indices["indices"]) >= 1
    time.sleep(1)


def test_getBhavCopyData_on_trade_holiday():
    with pytest.raises(BhavCopyNotFound):
        b.getBhavCopyData(datetime.date(2024, 1, 26))


def test_getBhavCopyData():
    bhavCopy = b.getBhavCopyData(datetime.date(2024, 1, 25))

    scripCodeTypes = {x["scripType"] for x in bhavCopy}

    predefinedScripCodeTypes = {"equity", "debenture", "preference", "bond"}

    assert scripCodeTypes == predefinedScripCodeTypes

    assert len(bhavCopy) > 0


def test_topGainers():
    topGainers = b.topGainers()

    assert len(topGainers) <= 5


def test_topLosers():
    topLosers = b.topLosers()

    assert len(topLosers) <= 5
