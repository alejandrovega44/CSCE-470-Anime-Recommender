#!/usr/bin/python

from pymongo import MongoClient
import cgi, cgitb
import json

cgitb.enable() # for trouble shooting
debug = False

#the cgi library gets var from html
data = cgi.FieldStorage()
print "Content-Type: text/html\n"
if debug:
    R_f=open('./incomingdata.txt','r')
    data=R_f.read()
    data= json.loads(data)
else:
    data =json.loads(data["RetrievedAnime"].value)

client = MongoClient() #get mongodb client
db= client.UpcomingAnime #get database named test_database
collection_Anime= db.Anime #get table named <insert name>  inside db named <insert name>

temp=[]
error=[]
for Name in data:
	if not collection_Anime.find({"a_name": Name}).count():
	    del data[Name]["i"]
	    temp.append(data[Name])
	else:
	    error.append( Name.encode("UTF-8"))

if len(temp) != 0:
    collection_Anime.insert(temp)
if len(error) != 0:
    print "Didn't insert the following since already in db \n "
    print json.dumps(error)
else:
   print "Db created succesfully"
