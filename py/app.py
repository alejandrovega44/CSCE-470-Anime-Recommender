#!/usr/bin/python

import cgi, cgitb
import os 
from functions import Functions
from pymongo import MongoClient
from textblob.classifiers import NaiveBayesClassifier
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
UpcomingData={}
for items in collection_Anime.find():
    UpcomingData[items["a_name"]]=items

#print "Content-Type: text/html\n"
if not debug:
    UserData= Functions.read_line( data["UserAnime"].value)
 
if debug and writeFile:
    U_f = open('./UserAnime', 'w')
    U_f.write(data["UserAnime"].value)
    U_f.close()
elif debug and not writeFile:
    U_f=open('./UserAnime', 'r')
    line=U_f.read()
    UserData= Functions.read_line(line)

cl = NaiveBayesClassifier(Functions.classify(UserData))
AnimeNames= UpcomingData.keys()
classifyData=Functions.newAnime(UpcomingData)
i=0
return_type={} #dictionary that will store all relevant animes be used to send back
for anime in classifyData:
    if cl.classify(anime) == "relevant":
        return_type[AnimeNames[i]]=UpcomingData[AnimeNames[i]]
    i+=1
#send back in json object the dictionary of relevant items
print json.dumps(return_type)
