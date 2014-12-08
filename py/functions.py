import json #or cjson
import re
from textblob.classifiers import NaiveBayesClassifier
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
	return train_t
	#return array of strings [("featueres,"relevant/unrelevant")]
    @staticmethod
    def stringData(Anime):
	#currently only taking to account genres
         featurelist={}
         for genre in Anime["a_genres"]:
	        featurelist[genre.encode("UTF-8").lower()] =True
	 for values in Anime["ppl"]:
		featurelist[values["name"]]=True
	 return featurelist
    @staticmethod
    def newAnime(NewAnime):
        test=[]
	filter = ["Light Novel", "TV", "Show", "Manga", "Original", "Video Game"]
	for Anime in NewAnime: 
	    temp={}
	    if not NewAnime[Anime]["generes"] == "":
	       genrelist= NewAnime[Anime]["generes"].encode("UTF-8").split()
	       for genre in genrelist:
	           temp[genre.lower()]=  True
	    if "ppl" in NewAnime[Anime].keys():
	        staff_list = NewAnime[Anime]["ppl"]
	        for i in staff_list:
	            staff_dict = i
	            if "name" in staff_dict.keys():
                        if staff_dict["name"].isdigit() == False and staff_dict["name"] not in filter:
                            temp[staff_dict["name"]] = True      
	           
	    test.append(temp)
        return test
    @staticmethod
    def classifyDescription(UserData,NewAnime):
    	featureVector=extractDesc(UserData,True)
    	cl = NaiveBayesClassifier(featureVector)
    	NewAnimeDescList=extractDesc(NewAnime, False)
    	relv_amount={}
    	i=0
    	for anime in NewAnimeDescList:
    		if (cl.classify(anime) == "relevant"):
    			relv_amount[i]=cl.prob_classify(anime).prob("relevant")
    	i+=1	
        #return an dict of  index : relevant score
        return relv_amount
    @staticmethod
    #takes in the data list of animes from user or upcoming and a bolean indicating if its the user data
    def extractDesc(Data,User):
    featureVector=[]
    if User: #create feature vector and classify
    	temp=Functions.findAvg(UserData)
		UserData=temp["dic"]
   		for anime in UserData:
		    if "desc" in anime.keys():
		        desc=anime["desc"].lower()
		    else:
		    	desc="none"
		    if UserData[Anime]["userRating"]-temp["score"]>= 0:
		    	#classify as relevant
	        	featureVector.append(( desc , 'relevant'))
		    else:
		        featureVector.append(( desc , 'unrelevant'))
    else: #create a vector with all descriptions for upcoming anime
    	for anime in Data:
		    if "desc" in anime.keys():
		        desc=anime["desc"].lower()
		    else:
		    	desc="none"
    		featureVector.append(desc)	
        #return an array of tuples with [(desc in lower case, relevant/unrelevant)..] if User
        #else return an array of desc [desc, desc, desc]
    return featureVector
if __name__ == '__main__':
    pass
