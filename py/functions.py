import json #or cjson
import re

class Functions(object):
    def __init__(slef):
        pass
        
    @staticmethod
    def read_line(a_json_string_from_document):
        #sample answer:
        return json.loads(a_json_string_from_document)

    @staticmethod
    def findAvg(UserData):
        #return an int and the dic with rating convt to number
	totalScore=0
	numScores=0
	for Anime in UserData:
    	    UserData[Anime]["userRating"] =int(UserData[Anime]["userRating"].encode("UTF-8"))
   	    totalScore+= UserData[Anime]["userRating"]
    	    numScores+=1
	return {"score": totalScore/numScores, "dic": UserData}   
    @staticmethod
    def classify(UserData):
	train_t=[]
        temp=Functions.findAvg(UserData)
	UserData=temp["dic"]
	for Anime in UserData:
	    if UserData[Anime]["userRating"]-temp["score"]>= 0:
	       train_t.append(( Functions.stringData(UserData[Anime]) , 'relevant'))
		#classify as relevant
	    else:
	        train_t.append(( Functions.stringData(UserData[Anime]) , 'unrelevant'))
		#classify as unrelevant
	#train={}
	#for animeList in train_t:
	#    for tuples in animeList:
	#        train.append(tuples)
	return train_t
	#return array of strings [("featueres,"relevant/unrelevant")]
    @staticmethod
    def stringData(Anime):
	#currently only taking to account genres
         featurelist={}
         for genre in Anime["a_genres"]:
	        featurelist[genre.encode("UTF-8")] =True
	 return featurelist
    @staticmethod
    def newAnime(NewAnime):
        test=[]
	for Anime in NewAnime: 
	    if not NewAnime[Anime]["generes"] == "":
	       genrelist= NewAnime[Anime]["generes"].encode("UTF-8").split()
	       temp={}
	       for genre in genrelist:
	           temp[genre]=  True
               test.append(temp)

        return test
if __name__ == '__main__':
    pass
