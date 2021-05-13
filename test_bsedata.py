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

import pytest
from bsedata.bse import BSE
from bsedata.exceptions import InvalidStockException

b = BSE(update_codes=True)

def test_str():
    assert str(b) == "Driver Class for Bombay Stock Exchange (BSE)"

def test_repr():
    assert repr(b) == "<BSE: update_codes=True> Driver Class for Bombay Stock Exchange (BSE)"

@pytest.mark.parametrize("scripCode",['534976','500116','512573'])
def test_getQuote_valid(scripCode):
    assert len(b.getQuote(scripCode)) == 27

def test_getQuote_invalid_default():
    with pytest.raises(InvalidStockException) as err_info:
        b.getQuote('513715')

    assert err_info.value.status == "Inactive stock"

def test_getQuote_invalid_custom():
    with pytest.raises(InvalidStockException) as err_info:
        b.getQuote('538936')

    assert err_info.value.status == "Suspended due to Procedural reasons"

def test_verifyCode_valid():
    assert b.verifyScripCode('534976') == 'V-mart Retail Ltd.'

def test_verifyCode_invalid():
    assert b.verifyScripCode('534980') == None

@pytest.mark.parametrize("timePeriod", ['1M', '3M', '6M', '12M'])
def test_getPeriodTrend(timePeriod):
    timePeriodResults = {
        '1M': [19, 30],
        '3M': [57, 90],
        '6M': [114, 180],
        '12M': [228, 360]
    }
    assert timePeriodResults[timePeriod][0] <= len(b.getPeriodTrend(
        '534976', timePeriod)) <= timePeriodResults[timePeriod][1]

def test_getPeriodTrend_invalid_period():
    with pytest.raises(AssertionError) as err_info:
        b.getPeriodTrend('534976', '2M')

    assert err_info.value.args[0] == "timePeriod should be one of the following options '1M', '3M', '6M' and '12M'"