import os
import io
import csv
import requests
import tempfile
import datetime
from zipfile import ZipFile
from bsedata.exceptions import BhavCopyNotFound
from bsedata.helpers import COMMON_REQUEST_HEADERS


def loadBhavCopyData(statsDate: datetime.date) -> list:
    tempDir = os.path.join(tempfile.gettempdir(), "bsedata")
    zipfileName = f"EQ{statsDate.strftime('%d%m%y')}_CSV.ZIP"
    r = requests.get(
        f"https://www.bseindia.com/download/BhavCopy/Equity/{zipfileName}",
        headers=COMMON_REQUEST_HEADERS,
    )

    if r.status_code != 200:
        raise BhavCopyNotFound()

    try:
        os.makedirs(tempDir)
    except FileExistsError:
        pass

    f_zip = open(os.path.join(tempDir, zipfileName), "wb+")
    f_zip.write(r.content)
    f_zip.close()

    output = []

    with ZipFile(os.path.join(tempDir, zipfileName)) as bhavCopyZip:
        with bhavCopyZip.open(f"EQ{statsDate.strftime('%d%m%y')}.CSV") as bhavCopyFile:
            reader = csv.DictReader(io.TextIOWrapper(bhavCopyFile))
            for row in reader:
                output.append(mapBhavCopyRowToDict(row))

    return output


def mapBhavCopyRowToDict(row: dict) -> dict:
    SC_TYPE_MAP = {"B": "bond", "Q": "equity", "D": "debenture", "P": "preference"}
    return {
        "scrip_code": row["SC_CODE"],
        "open": row["OPEN"],
        "high": row["HIGH"],
        "low": row["LOW"],
        "close": row["CLOSE"],
        "last": row["LAST"],
        "prev_close": row["PREVCLOSE"],
        "total_trades": row["NO_TRADES"],
        "total_shares_traded": row["NO_OF_SHRS"],
        "net_turnover": row["NET_TURNOV"],
        "scrip_type": SC_TYPE_MAP[row["SC_TYPE"]],
    }
