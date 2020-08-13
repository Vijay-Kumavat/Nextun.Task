# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 21:58:13 2020

@author: vijay
"""


import pandas as pd #import python libary-pandas
import mysql.connector #import mysql

mydb=mysql.connector.connect(host='next.cmzxorbdsjvq.us-east-2.rds.amazonaws.com',user='user',passwd='test1234',db='classicmodels')

df=pd.read_sql(sql='select * from customers',con=mydb) 
df

df1=pd.read_sql(sql='select * from employees',con=mydb)
df1

df2=pd.read_sql(sql='select * from offices',con=mydb)
df2 


df3=pd.read_sql(sql='select * from orderdetails',con=mydb)
df3

df4=pd.read_sql(sql='select * from orders',con=mydb)
df4

df5=pd.read_sql(sql='select * from payments',con=mydb)
df5

df6=pd.read_sql(sql='select * from productlines',con=mydb)
df6

df7=pd.read_sql(sql='select * from products',con=mydb)
df7

