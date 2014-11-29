#!/usr/bin/python

import cgi, cgitb
import os 
from functions import Functions
from pymongo import MongoClient
#cgitb.enable()  # for troubleshooting

#the cgi library gets vars from html
data = cgi.FieldStorage()
#this is the actual output
debug = True
writeFile = False

#retrieving data from mongodb 
client = MongoClient() #get mongodb client
db= client.UpcomingAnime #get database named test_database
collection_Anime= db.Anime #get table named <insert name>  inside db named <insert name>
#create upcoming anime dictionary 
temp={}
for items in collection_Anime.find():
    temp[items["a_name"]]=items

print "Content-Type: text/html\n"
if not debug:
    print "User Animelist: " + data["UserAnime"].value
 
if debug and writeFile:
    U_f = open('./UserAnime', 'w')
    U_f.write(data["UserAnime"].value)
    U_f.close()
elif debug and not writeFile:
    U_f=open('./UserAnime', 'r')
    line=U_f.read()
print temp
