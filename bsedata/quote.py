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

from bs4 import BeautifulSoup as bs
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'
}

def quote(scripCode):
    baseurl = '''https://m.bseindia.com/StockReach.aspx?scripcd='''
    res = requests.get(baseurl + scripCode, headers=headers)
    c = res.content
    soup = bs(c, "lxml")

    res = {}

    for span in soup('span'):
        try:
            if span['class'][0] == 'srcovalue':
                try:
                    if span['id'] == 'spanchangVal':
                        res['change'] = span.string.split('(')[0].strip()
                        res['pChange'] = span.string.split('(')[1].strip()[:-2]
                except AttributeError:
                    res['change'] = ''
                    res['pchange'] = ''
                except KeyError:
                    res['currentValue'] = span.strong.string
            elif span['class'][0] == 'companyname':
                res['companyName'] = span.string
        except KeyError:
            try:
                if span['id'] == 'lblPBdate':
                    try:
                        res['priceBand'] = span.string.split(':')[1].strip()
                    except AttributeError:
                        res['priceBand'] = ''
                elif span['id'] == 'strongDate':
                    res['updatedOn'] = span.string.split('-')[1].strip()
            except KeyError:
                continue

    for td in soup('td'):
        try:
            if td['id'] == 'tdCShortName':
                try:
                    res['securityID'] = td.string.strip()
                except AttributeError:
                    res['securityID'] = ''
            elif td['id'] == 'tdscripcode':
                try:
                    res['scripCode'] = td.string.strip()
                except AttributeError:
                    res['scripCode'] = ''
            elif td['id'] == 'tdgroup':
                try:
                    res['group'] = td.string.strip()
                except AttributeError:
                    res['group'] = ''
            elif td['id'] == 'tdfacevalue':
                try:
                    res['faceValue'] = td.string.strip()
                except AttributeError:
                    res['faceValue'] = ''
            elif td['id'] == 'tdIndustry':
                try:
                    res['industry'] = td.string.strip()
                except AttributeError:
                    res['industry'] = ''
            elif td['id'] == 'tdpcloseopen':
                try:
                    res['previousClose'] = td.string.split("/")[0].strip()
                    res['previousOpen'] = td.string.split("/")[1].strip()
                except AttributeError:
                    res['previousClose'] = ''
                    res['previousOpen'] = ''
            elif td['id'] == 'tdDHL':
                try:
                    res['dayHigh'] = td.string.split("/")[0].strip()
                    res['dayLow'] = td.string.split("/")[1].strip()
                except AttributeError:
                    res['dayHigh'] = ''
                    res['dayLow'] = ''
            elif td['id'] == 'td52WHL':
                try:
                    res['52weekHigh'] = td.string.split("/")[0].strip()
                    res['52weekLow'] = td.string.split("/")[1].strip()
                except AttributeError:
                    res['52weekHigh'] = ''
                    res['52weekLow'] = ''
            elif td['id'] == 'tdWAp':
                try:
                    res['weightedAvgPrice'] = td.string.strip()
                except AttributeError:
                    res['weightedAvgPrice'] = ''
            elif td['id'] == 'tdTTV':
                try:
                    res['totalTradedValue'] = td.string.strip() + " Cr."
                except AttributeError:
                    res['totalTradedValue'] = '0' + " Cr."
            elif td['id'] == 'tdTTQW':
                try:
                    res['totalTradedQuantity'] = td.string.split("/")[0].strip() + " Lakh"
                    res['2WeekAvgQuantity'] = td.string.split("/")[1].strip() + " Lakh"
                except AttributeError:
                    res['totalTradedQuantity'] = '0' + " Lakh"
                    res['2WeekAvgQuantity'] = '0' + " Lakh"
            elif td['id'] == 'tdMktCapVal':
                try:    
                    res['marketCapFull'] = td.string.split("/")[0].strip() + " Cr."
                    res['marketCapFreeFloat'] = td.string.split("/")[1].strip() + " Cr."
                except AttributeError:
                    res['marketCapFull'] = '0' + " Cr."
                    res['marketCapFreeFloat'] = '0' + " Cr."
        except KeyError:
            continue

    if res['priceBand'] != '':
        for tbody in soup('tbody'):
            try:
                if tbody['id'] == 'PBtablebody':
                    data = tbody.contents[2]
                    res['upperPriceBand'] = data.contents[1].string.strip()
                    res['lowerPriceBand'] = data.contents[2].string.strip()
            except KeyError:
                continue
    else:
        res['upperPriceBand'] = ''
        res['lowerPriceBand'] = ''

    buy = {}
    sell = {}
    for td in soup('td'):
        try:
            if td['id'] == 'tdBQ1':
                buy['1'] = {"quantity": td.string, "price": td.next_sibling.next_sibling.string}
            elif td['id'] == 'tdBQ2':
                buy['2'] = {"quantity": td.string, "price": td.next_sibling.next_sibling.string}
            elif td['id'] == 'tdBQ3':
                buy['3'] = {"quantity": td.string, "price": td.next_sibling.next_sibling.string}
            elif td['id'] == 'tdBQ4':
                buy['4'] = {"quantity": td.string, "price": td.next_sibling.next_sibling.string}
            elif td['id'] == 'tdBQ5':
                buy['5'] = {"quantity": td.string, "price": td.next_sibling.next_sibling.string}
            elif td['id'] == 'tdSP1':
                sell['1'] = {"price": td.string, "quantity": td.next_sibling.next_sibling.string}
            elif td['id'] == 'tdSP2':
                sell['2'] = {"price": td.string, "quantity": td.next_sibling.next_sibling.string}
            elif td['id'] == 'tdSP3':
                sell['3'] = {"price": td.string, "quantity": td.next_sibling.next_sibling.string}
            elif td['id'] == 'tdSP4':
                sell['4'] = {"price": td.string, "quantity": td.next_sibling.next_sibling.string}
            elif td['id'] == 'tdSP5':
                sell['5'] = {"price": td.string, "quantity": td.next_sibling.next_sibling.string}
        except KeyError:
            continue
    res['buy'] = buy
    res['sell'] = sell

    return res
