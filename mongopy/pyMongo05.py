#!/usr/bin/python3
"""Deleting MongoDB data with Python || RZFeeser@alta3.com"""

from pymongo import MongoClient
#include pprint for readabillity of the 
from pprint import pprint

def main():
    #change the MongoClient connection string to your MongoDB database instance
    client = MongoClient(port=27017)
    db = client.business

    # this will remove all entries in the database "business"
    result = db.reviews.drop()

if __name__ == "__main__":
    main()

