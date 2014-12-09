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
debug = False
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
    U_f = open('./UserAnime', 'w')
    U_f.write(data["UserAnime"].value)
    U_f.close()
elif debug and not writeFile:
    U_f=open('./UserAnime', 'r')
    line=U_f.read()
    UserData= Functions.read_line(line)
train= Functions.classify(UserData)
# array of tuples holding a (dict of genres genre:true, relevant/nonrelevant)
if debug: 
    print "size of training array:" +str(len(train))
    rel=[]
    unrelev=[]
    for tup in train:
        if tup[1] == "relevant":
    	    rel.append(tup)
        else: 
	    unrelev.append(tup)
    print "the relevant length "+str(len(rel))
    print "the unrelevant length" +str(len(unrelev))
cl = nltk.classify.naivebayes.NaiveBayesClassifier.train(train)
AnimeNames= UpcomingData.keys()
classifyData=Functions.newAnime(UpcomingData) # an array of arrays of single gengres
i=0
return_type=[] #dictionary that will store all relevant animes be used to send back
relv_amount={}
for anime in classifyData:
    if (cl.classify(anime) == "relevant"):
        if debug:
	    print "Name: " + AnimeNames[i].encode("UTF-8")
        relv_amount[i]=cl.prob_classify(anime).prob("relevant")
    elif debug:
	if debug:
	    print "unrelevant"+ AnimeNames[i].encode("UTF-8")
    if debug:
        prob_dist = cl.prob_classify(anime)
        print "relevant " + str(prob_dist.prob("relevant"))
        print "unrelevant " + str(prob_dist.prob("unrelevant"))
    i+=1
sorted_relevances = sorted(relv_amount, key=relv_amount.get, reverse=True)
if debug:
    print "number of relevant animes:" +str(len(sorted_relevances))
if debug:
    print sorted_relevances
for i in sorted_relevances[:6]:
    return_type.append(UpcomingData[AnimeNames[i]])
    if debug:
        print AnimeNames[i].encode("UTF-8")
#send back in json object the dictionary of relevant items
print json.dumps(return_type).encode("UTF-8")

#if debug:
#    cl.show_informative_features()
