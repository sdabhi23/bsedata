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


class InvalidStockException(Exception):
    """
    Exception raised for stocks which have been suspended or no longer trading on BSE.

    :param status: the status of the stock as mentioned on BSE website
    """

    def __init__(self, status: str = "Inactive stock"):
        if status == "":
            self.status = "Inactive stock"
        else:
            self.status = status
        super().__init__(self.status)


class BhavCopyNotFound(Exception):
    """
    Exception raised when the BhavCopy file is not found on BSE website.
    """

    def __init__(self):
        super().__init__(
            """The BhavCopy file was not found on the BSE website. You are probably trying to get data for a trading holiday."""
        )
