#!/usr/bin/python3
"""Updating MongoDB with Python || RZFeeser@alta3.com"""

from pymongo import MongoClient
#include pprint for readabillity of the 
from pprint import pprint

def main():
    #change the MongoClient connection string to your MongoDB database instance
    client = MongoClient(port=27017)
    db=client.business

    #choose a single review from our db
    ASingleReview = db.reviews.find_one({})
    print('A sample document:')
    pprint(ASingleReview)

    #update the review by a single like
    result = db.reviews.update_one({'_id' : ASingleReview.get('_id') }, {'$inc': {'likes': 1}})
    print('Number of documents modified : ' + str(result.modified_count))

    #create an updated document object
    UpdatedDocument = db.reviews.find_one({'_id':ASingleReview.get('_id')})
    print('The updated document:')
    pprint(UpdatedDocument)

if __name__ == "__main__":
    main()

