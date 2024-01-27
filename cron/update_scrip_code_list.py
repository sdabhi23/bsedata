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

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

import os
import sys
import json
import logging
import pandas as pd

logging.basicConfig(
    stream=sys.stdout,
    format="%(filename)s:%(lineno)d - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logging.info("Loading CSV from NASDAQ")

df = pd.read_csv(
    "https://data.nasdaq.com/api/v3/databases/BSE/metadata?api_key=5jiXMkYN6mW7fVm6ExGo",
    compression="zip",
    header=0,
    sep=",",
    quotechar='"',
).drop(columns=["description", "refreshed_at", "from_date", "to_date"])

logging.info("Loaded CSV from NASDAQ")

logging.info("Processing stock codes")

stk_df = df[df.code.astype(str).str.contains("BOM")].reset_index(drop=True)

stk_final = {
    x["code"].replace("BOM", ""): x["name"].split("EOD")[0].strip().replace("-$", "")
    for x in stk_df.to_dict(orient="records")
}

logging.info("Verifying stock codes")

for stk_code in stk_final.keys():
    assert len(stk_code) == 6

logging.info("Saving stock codes to file")

f_stk = open("stk.json", "w+")
f_stk.write(json.dumps(stk_final))
f_stk.close()

logging.info("Processing index codes")

indices_df = df[~df.code.astype(str).str.contains("BOM")].reset_index(drop=True)

indices_final = {x["code"]: x["name"] for x in indices_df.to_dict(orient="records")}

logging.info("Saving index codes to file")

f_indices = open("indices.json", "w+")
f_indices.write(json.dumps(indices_final))
f_indices.close()

logging.info("Uploading files to R2")

import boto3

s3 = boto3.client(
    service_name="s3",
    endpoint_url=f"https://{os.environ['CLOUDFLARE_ACCOUNT_ID']}.r2.cloudflarestorage.com",
    aws_access_key_id=os.environ["R2_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["R2_SECRET_ACCESS_KEY"],
    region_name="apac",
)

s3.upload_file(Filename="./stk.json", Bucket="bsedata", Key="stk.json")
s3.upload_file(Filename="./indices.json", Bucket="bsedata", Key="indices.json")
