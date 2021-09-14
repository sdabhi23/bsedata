"""

    MIT License

    Copyright (c) 2019 Paul Antony

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


import json
import requests
from bs4 import BeautifulSoup as bs

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'
}

def getFinancialData(scripCode, trendPeriod, scale):
    assert trendPeriod in ['Qtly', 'Ann'], "trendType should be one of the following options 'Qtly' or 'Ann'"
    assert scale in ['Cr', 'M'], "scale should be one of the following options 'Cr' or 'M'"

    baseurl = '''https://api.bseindia.com/BseIndiaAPI/api/GetReportNewFor_Result/w?scripcode='''
    res = requests.get(baseurl + scripCode, headers=headers)

    data = json.loads(res.content.decode('utf-8'))

    datakey = trendPeriod + 'in' + scale

    c = data[datakey]
    soup = bs(c, "lxml")

    table = []

    for tr in soup.find_all('tr'):
        row = []
        for td in tr.find_all('td'):
            row.append(td.string)
        table.append(row);

    datalen = len(table[0])
    attribLen = 14;
    
    result = []
    for i in range(1, datalen):
        datasegment = {}
        datasegment['Period']       = table[0][i]
        datasegment['Revenue']      = float(table[2][i].replace(",", "").replace("--","0"))
        datasegment['OtherIncome']  = float(table[3][i].replace(",", "").replace("--","0"))
        datasegment['TotalIncome']  = float(table[4][i].replace(",", "").replace("--","0"))
        datasegment['Expenditure']  = float(table[5][i].replace(",", "").replace("--","0"))
        datasegment['Interest']     = float(table[6][i].replace(",", "").replace("--","0"))
        datasegment['PBDT']         = float(table[7][i].replace(",", "").replace("--","0"))
        datasegment['Depreciation'] = float(table[8][i].replace(",", "").replace("--","0"))
        datasegment['PBT']          = float(table[9][i].replace(",", "").replace("--","0"))
        datasegment['Tax']          = float(table[10][i].replace(",", "").replace("--","0"))
        datasegment['NetProfit']    = float(table[11][i].replace(",", "").replace("--","0"))
        datasegment['Equity']       = float(table[12][i].replace(",", "").replace("--","0"))
        datasegment['EPS']          = float(table[13][i].replace(",", "").replace("--","0"))
        datasegment['CEPS']         = float(table[14][i].replace(",", "").replace("--","0"))
        datasegment['OPM ']         = float(table[15][i].replace(",", "").replace("--","0"))
        datasegment['NPM  ']        = float(table[16][i].replace(",", "").replace("--","0"))

        result.append(datasegment)

    
    return result

