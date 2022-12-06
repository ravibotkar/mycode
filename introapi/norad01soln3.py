#!/usr/bin/python3
"""Alta3 Research | RZfeeser@alta3.com
   CHALLENGE 02 (SOLUTION) - Transform Norad data into JSON"""

from datetime import datetime
from io import StringIO
import json

import requests
import pandas as pd

URL = "http://www.celestrak.com/NORAD/elements/active.txt"


def data_getter(url):
    """perform a lookup to a URI and determine if the lookup was valid"""
    resp = requests.get(url)
    if resp.status_code != 200:     # if we didn't get back a 200...
        return None
    else:
        return StringIO(resp.text)  # without this the /r/n are unrecognized

def norad_preprocessing(chunk):
    """make changes / tweaks to a data chonk"""
    try:
        # renaming shouldn't be necessary, should be able to do this within read_csv()
        res = dict(zip(chunk.index.values, ['name','nav1','nav2']))    # index values keep changing, so we need to figure them out and map to new names
        chunk.rename(index=res, inplace=True)
        chunk = chunk.T # transpose the col and records (same as chunk = chunk.transpose())
        return chunk.to_dict(orient='index').get(0)
    except:
        return None

def main():
    """run-time code"""

    # HTTP GET the dataset
    data = data_getter(URL)
    # HTTP checking
    if not data:
        print("Seems like there was an error with the HTTP operation.")
        return


    # this is not a dataframe, but an object for further operation in our next step
    #df_chunk = pd.read_csv(data, sep=" ", header=None, chunksize=3)
    df_chunk = pd.read_csv(data, sep="/n", header=None, chunksize=3, engine='python')

    # we will append each chunk df here
    chonk_list = []

    # grab one of these chonks and and process it
    for chunk in df_chunk:
        # tweak 3 lines into JSON
        chunk_filter = norad_preprocessing(chunk)
        # Chunk checking
        if not chunk_filter:
            print("Seems like there was an error with pandas creating JSON data.")
            return
        else:
            chonk_list.append(chunk_filter)


    # should be legal python dict
    norad = {datetime.today().strftime('%Y-%m-%d'): chonk_list}

    # render to JSON file
    with open("norad.json", "w") as noradjson:
        json.dump(norad, noradjson)

if __name__ == "__main__":
    main()

