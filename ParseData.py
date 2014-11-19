import json,ast #or cjson
from math import log,sqrt
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class Recommender(object):
	def __init__(self):
	
		self.UserStaff = {}
		self.GenStaff = {}
		self.UserDesc = {}
		self.GenDesc = {}
		self.GenComp = {} 
		self.UserComp = {} 
		
	def read_line(self, json_string):
		return ast.literal_eval(json_string)

	def read_json_file(self, file):
		animelist = [] 
		for line in open(file, 'r'):
			line = line.split(' ', 1)
			type = line[0]
			dict = self.read_line(line[1])
			animelist.append([type, dict])
		return animelist 
		
	def init(self, Animelist):
		 
		#Dict associated with given keys (UserAnime, GeneratedAnime) 
		User = Animelist[0]
		Gen = Animelist[1]
		
		#keys: UserAnime, GeneratedAnime 
		UserType = User[0]
		GenType = Gen[0]
		
		#Dict of anime information 
		UserAnimes = User[1]
		GenAnimes = Gen[1] 
		
		#vars for user anime list 
		ani_desc = [] 
		ani_staff = [] 
		ani_genres = [] 
		ani_staff = []
		
		#var for generated anime list 
		g_desc = [] 
		g_staff = [] 
		g_genres = [] 
		g_staff = []
		g_comp = [] 
		genre_count = {}
		u_rating = {} 
		
		#iterating through the user's anime list 
		for anime, dict in UserAnimes.items():
			#grab the values of each key if they exists 
			if "desc" in dict.keys():
				ani_desc.append(dict["desc"])
			
			if "ppl" in dict.keys():
				member = dict["ppl"] 
				member = member.split(":")
				for items in member:
					staff_member = items.split("\n")
					if staff_member[0] != '':
						ani_staff.append(staff_member[0])
						
			if "a_genres" in dict.keys():
				for items in dict["a_genres"]:
					ani_genres.append(items)
			
			#get genre counts for that rating, sum the scores then divide by the count 
			
			if "userRating" in dict.keys():
				if "a_genres" in dict.keys():
					genre_list = dict["a_genres"] 
					for genre in genre_list:
						if genre not in genre_count:
							genre_count[genre] = 1
							u_rating[genre] = int(dict["userRating"])
						else:
							genre_count[genre] += 1
							u_rating[genre] += int(dict["userRating"])
		
		for ani_genre in u_rating.keys():
			avg_rating = u_rating[ani_genre]/genre_count[ani_genre]
			u_rating[ani_genre] = avg_rating
		
		
		#processing data retrieved 
		self.initStaff(ani_staff)
		self.initDesc(ani_desc, UserType)
	
		#need to pair a_name with processed data (do the func call within the loop and append and form key: dict 
		#iterating throug the generated anime list 	
		for g_anime, g_dict in GenAnimes.items():
			#grab the values of each key if they exists 
			if "desc" in g_dict.keys():
				g_desc.append(g_dict["desc"])
			
			if "ppl" in g_dict.keys():
				staff_dict = g_dict["ppl"]
				# for k in staff_dict.keys():
					# print k
						
			if "a_generes" in g_dict.keys():
				for items in g_dict["a_generes"]:
					if items != ",": 
						if "," not in items: 
							g_genres.append(items)
						if "," in items: 
							str = items.replace(",", " ")
							str = " ".join(str.split())
							g_genres.append(str)
			
			if "company" in g_dict.keys():
				comp_dict =  g_dict["company"]
				if "name" in comp_dict.keys():
					g_comp.append(comp_dict["name"])
		
		#processing data retrieved 
		self.initCompany(g_comp, GenType)

					
	def initDesc(self, desc_list, type):
		stopset = set(stopwords.words('english'))
		tokenlist = [] 
		
		for string in desc_list:
			tokens = word_tokenize(str(string))
			for words in tokens:
				if words in stopset:
					tokens.remove(words)	
				
				elif words.isalpha() == False:
					tokens.remove(words)
				
				else:
					tokenlist.append(words)
		
		#getting raw counts of each token 
		if type == "UserAnime":
			for words in tokenlist: 
				if words not in self.UserDesc:
					self.UserDesc[words] = 1
				else:
					self.UserDesc[words] += 1
		
		if type == "GeneratedAnime":
			for token in tokenlist:
				if token not in self.GenDesc:
					self.GenDesc[token] = 1
				else:
					self.GenDesc[token] += 1 
		
			
			
	def initCompany(self, comp_dict, type):
		
		#getting raw counts of each token 
		if type == "UserAnime": 
			for name in comp_dict:
				if name not in self.UserComp:
					self.UserComp[name] = 1 
				else:
					self.UserComp[name] += 1
				
		if type == "GeneratedAnime": 
			for name in comp_dict:
				if name not in self.GenComp:
					self.GenComp[name] = 1 
				else:
					self.GenComp[name] += 1
			
		
		
	def InitRatings():
		pass

	def initStaff(self, staff_list):
		#getting raw counts of each token 
		for s in staff_list:
			if s not in self.UserStaff:
				self.UserStaff[s] = 1 
			else:
				self.UserStaff[s] += 1
		
	

			
if __name__ == "__main__":

	rec = Recommender() 
	file = "RecOutput.json"
	Animelist = rec.read_json_file(file)
	parseAnimes = rec.init(Animelist)
	
	
	