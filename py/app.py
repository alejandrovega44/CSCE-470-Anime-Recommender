#!/usr/bin/python
import cgi, cgitb
import os 
from functions import Functions
from pymongo import MongoClient
import nltk
import json
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
    del items["_id"]
    UpcomingData[items["a_name"]]=items
   
print "Content-Type: text/html\n"
if not debug:
    UserData= Functions.read_line( data["UserAnime"].value)
 
if debug and writeFile:
    U_f = open('./UserAnime2', 'w')
    U_f.write(data["UserAnime"].value)
    U_f.close()
elif debug and not writeFile:
    U_f=open('./UserAnime2', 'r')
    line=U_f.read()
    UserData= Functions.read_line(line)
train= Functions.classify(UserData)
# array of tuples holding a (genre, relevant/nonrelevant)
cl = nltk.classify.naivebayes.NaiveBayesClassifier.train(train)
AnimeNames= UpcomingData.keys()
print train
classifyData=Functions.newAnime(UpcomingData) # an array of arrays of single gengres
i=0
return_type=[] #dictionary that will store all relevant animes be used to send back
#prob_dist = classifier.prob_classify
print classifyData
for anime in classifyData:
    print anime
    print cl.classify(anime)
    if cl.classify(anime) == "relevant":
        if debug:
	    print "relevant " + AnimeNames[i].encode("UTF-8")
	    print anime
	    prob_dist = cl.prob_classify(anime)
	    print "relevant " + str(prob_dist.prob("relevant"))
	    print "unrelevant " + str(prob_dist).prob("unrelevant"))
	return_type.append(UpcomingData[AnimeNames[i]])
    elif debug:
	print "unrelevant"+ AnimeNames[i].encode("UTF-8")
    i+=1
#send back in json object the dictionary of relevant items
#print json.dumps(return_type).encode("UTF-8")

#if debug:
#    cl.show_informative_features()
