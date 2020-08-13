# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 22:08:12 2020

@author: vijay
"""
import pymongo
import pandas as pd
#import numpy as np

client=pymongo.MongoClient("mongodb+srv://vijay:NXZp2yaELqd6aCGu@next.zgtwo.mongodb.net/sample_airbnb?retryWrites=true&w=majority")
db=client['sample_airbnb']
col=db['listingsAndReviews']

df=col.find()

for data in df: 
    print(data) 