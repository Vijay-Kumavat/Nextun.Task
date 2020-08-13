import pandas as pd #import python libary-pandas
import mysql.connector #import mysql

mydb=mysql.connector.connect(host='next.cmzxorbdsjvq.us-east-2.rds.amazonaws.com',user='user',passwd='test1234',db='classicmodels') #connect mysql.connector with pandas using connect method

df=pd.read_sql(sql='select * from customers',con=mydb) #read the sql query using pandas df #customers
df.to_excel('MySQLTask_customers.xlsx') #MySQL Table data export into excel file, #index=flase then index is not showing in xlsx file

df=pd.read_sql(sql='select * from employees',con=mydb) #read the sql query using pandas df #employees
df.to_excel('MySQLTask_employees.xlsx') #MySQL Table data export into excel file, #index=flase then index is not showing in xlsx file

df=pd.read_sql(sql='select * from offices',con=mydb) #read the sql query using pandas df #offices
df.to_excel('MySQLTask_offices.xlsx') #MySQL Table data export into excel file, #index=flase then index is not showing in xlsx file

df=pd.read_sql(sql='select * from orderdetails',con=mydb) #read the sql query using pandas df #orderdetails
df.to_excel('MySQLTask_orderdetails.xlsx') #MySQL Table data export into excel file, #index=flase then index is not showing in xlsx file

df=pd.read_sql(sql='select * from orders',con=mydb) #read the sql query using pandas df #orders
df.to_excel('MySQLTask_orders.xlsx') #MySQL Table data export into excel file, #index=flase then index is not showing in xlsx file

df=pd.read_sql(sql='select * from payments',con=mydb) #read the sql query using pandas df #payments
df.to_excel('MySQLTask_payments.xlsx') #MySQL Table data export into excel file, #index=flase then index is not showing in xlsx file

df=pd.read_sql(sql='select * from productlines',con=mydb) #read the sql query using pandas df #productlines
df.to_excel('MySQLTask_productlines.xlsx') #MySQL Table data export into excel file, #index=flase then index is not showing in xlsx file

df=pd.read_sql(sql='select * from products',con=mydb) #read the sql query using pandas df #products
df.to_excel('MySQLTask_products.xlsx') #MySQL Table data export into excel file, #index=flase then index is not showing in xlsx file