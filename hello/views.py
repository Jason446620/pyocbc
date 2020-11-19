from django.http import HttpResponse
from django.shortcuts import render

import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:panshubeisqlserver.database.windows.net,1433' 
database = 'jasonp2db' 
username = 'sasasa' 
password = 'Jason.446620' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#Sample select query
cursor.execute("SELECT TOP (1) * FROM [dbo].[DBS]") 
row = cursor.fetchone() 
result='';
while row: 
    print(row[2])
    result=row[2]
    row = cursor.fetchone()

def hello(request):
    return HttpResponse(result)
