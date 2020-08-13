# import pymongo

# connection = pymongo.MongoClient('localhost',27017)

# database=connection['sample_airbnb']

import pymongo
import pandas as pd
import numpy as np

client=pymongo.MongoClient("mongodb+srv://vijay:NXZp2yaELqd6aCGu@next.zgtwo.mongodb.net/sample_airbnb?retryWrites=true&w=majority")
db=client['sample_airbnb']
col=db['listingsAndReviews']

df=col.find()

for data in df: 
    print(data)


# mycol=mydb.mycol.find()

# df=pd.DataFrame(list(mycol))

# df=pd.DataFrame(list(mydb.listingsAndReviews.find()))


# df=pd.read_csv('kumavat.csv')

# df=mycol
# data = pd.DataFrame

# df.to_csv('friend.csv')

# df = pymongo.read_mongo("listingsAndReviews", [], "mongodb://localhost:27017/sample_airbnb")

# # mycol.to_excel(mycoltoexcel,sheet_name='Sheet1')

# mycoltoexcel.save()

# make an API call to the MongoDB server
# cursor = col.find()

# # extract the list of documents from cursor obj
# mongo_docs = list(cursor)

# # restrict the number of docs to export
# mongo_docs = mongo_docs[:50] # slice the list
# print ("total docs:", len(mongo_docs))

# # create an empty DataFrame for storing documents
# docs = pandas.DataFrame(columns=[])

# # iterate over the list of MongoDB dict documents
# for num, doc in enumerate(mongo_docs):

# # convert ObjectId() to str
# doc["_id"] = str(doc["_id"])

# # get document _id from dict
# doc_id = doc["_id"]

# # create a Series obj from the MongoDB dict
# series_obj = pandas.Series( doc, name=doc_id )

# # append the MongoDB Series obj to the DataFrame obj
# docs = docs.append(series_obj)

# # only print every 10th document
# if num % 10 == 0:
# print (type(doc))
# print (type(doc["_id"]))
# print (num, "--", doc, "\n")

# "
# EXPORT THE MONGODB DOCUMENTS
# TO DIFFERENT FILE FORMATS
# "
# print ("\nexporting Pandas objects to different file types.")
# print ("DataFrame len:", len(docs))

# # export the MongoDB documents as a JSON file
# docs.to_json("object_rocket.json")

# # have Pandas return a JSON string of the documents
# json_export = docs.to_json() # return JSON data
# print ("\nJSON data:", json_export)

# # export MongoDB documents to a CSV file
# docs.to_csv("object_rocket.csv", ",") # CSV delimited by commas

# # export MongoDB documents to CSV
# csv_export = docs.to_csv(sep=",") # CSV delimited by commas
# print ("\nCSV data:", csv_export)


