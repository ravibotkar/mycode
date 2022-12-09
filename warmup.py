#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
from pprint import pprint

x= 3
URL= f"https://opentdb.com/api.php?amount={x}&type=multiple"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()
   # pprint(data)
  # pprint(data["results"][0]["incorrect_answers"])
    #print(data["results"])
    for l in data["results"]:
        pprint(l["question"])
        pprint(l["correct_answer"])
        pprint(l["incorrect_answers"])
        #pprint(data["results"][i]["correct_answer"])
        #pprint(data["results"][i]["incorrect_answers"])
    #pprint(data["results"][0]["correct_answer"])
    #pprint(data["results"][0]["incorrect_answers"])
    #pprint(data["results"][1]["correct_answer"])
    #pprint(data["results"][1]["incorrect_answers"])
    #pprint(data["results"][2]["correct_answer"])
    #pprint(data["results"][2]["incorrect_answers"])   


if __name__ == "__main__":
    main()
