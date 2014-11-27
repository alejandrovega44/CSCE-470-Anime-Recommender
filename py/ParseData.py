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
		self.GenGenre = {} 
		self.UserGenre = {} 
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
	
	def initGenAnime(self, Animelist):
	
		#vars for Generated list 
		g_desc = [] 
		g_staff = [] 
		g_genres = [] 
		g_staff = []
		g_comp = [] 
		
		desc_dict = {}
		ppl_dict = {} 
		genre_dict = {} 
		s_list = [] 
		company_dict = {} 
		
		#Dict associated with given keys (GeneratedAnime) 
		Gen = Animelist[1]
		
		#Dict of generated Animes 
		GenAnimes = Gen[1] 
		
		#key: GeneratedAnime
		GenType = Gen[0]
		
		filter = ["Light Novel", "TV", "Show", "Manga", "Original", "Video Game"]
		
		#iterating through the generated anime list 	
		for g_anime, g_dict in GenAnimes.items():
			#grab the values of each key if they exists 
			if "desc" in g_dict.keys():
				desc = g_dict["desc"]
				g_desc.append(desc)
				desc_dict[g_anime] = g_desc
				g_desc = [] 
			
			#anime did not have a desc, 1 is a placeholder will 
			elif "desc" not in g_dict.keys():
				desc_dict[g_anime] = 1
			
			if "ppl" in g_dict.keys():
				staff_list = g_dict["ppl"]
				for i in staff_list:
					staff_dict = i 
					if "name" in staff_dict.keys():
						if staff_dict["name"].isdigit() == False and staff_dict["name"] not in filter:
							s_list.append(staff_dict["name"])
				ppl_dict[g_anime] = s_list
				s_list = [] 
							
						
			if "a_generes" in g_dict.keys():
				for items in g_dict["a_generes"]:
					if items != ",": 
						if "," not in items: 
							g_genres.append(items)
						if "," in items: 
							str = items.replace(",", " ")
							str = " ".join(str.split())
							g_genres.append(str)
				genre_dict[g_anime] = g_genres
				g_genres = [] 
			
			elif "a_generes" in g_dict.keys():
				genre_dict[g_anime] = 1 
				
			
			if "company" in g_dict.keys():
				comp_dict =  g_dict["company"] 
				if "name" in comp_dict.keys():
					g_comp.append(comp_dict["name"])
					company_dict[g_anime] = g_comp 
					g_comp = [] 
				elif "name" not in comp_dict.keys():
					company_dict[g_anime] = 1
					
			
		
		#processing data retrieved
		self.initCompany(company_dict, GenType)
		self.initDesc(desc_dict, GenType) 
		self.initStaff(ppl_dict, GenType)
		self.initGenres(genre_dict, GenType)
		
	def initUserAnime(self, Animelist):
		
		#vars for user anime list 
		ani_desc = [] 
		ani_genres = [] 
		ani_staff = []
		ani_comp = [] 
		genre_count = {}
		u_rating = {} 
		 
		#Dict associated with given keys (UserAnime) 
		User = Animelist[0]
		
		#key: UserAnime
		UserType = User[0]
		
		#Dict of anime information 
		UserAnimes = User[1]

		#iterating through the user's anime list 
		for anime, dict in UserAnimes.items():
			#grab the values of each key if they exists 
			if "desc" in dict.keys():
				ani_desc.append(dict["desc"])
			
			if "ppl" in dict.keys():
				ppl_list = dict["ppl"]
				for staff in ppl_list:
					if "name" in staff.keys(): 
						ani_staff.append(staff["name"])
						
				
			if "a_genres" in dict.keys():
				for items in dict["a_genres"]:
					ani_genres.append(items)
			
			if "company" in dict.keys():
				comp_list = dict["company"]
				for comp in comp_list:
					ani_comp.append(comp)
					
			
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
		self.initCompany(ani_comp, UserType)
		self.initStaff(ani_staff, UserType)
		self.initDesc(ani_desc, UserType)
		self.initGenres(ani_genres, UserType) 

					
	def initDesc(self, desc_list, type):
		stopset = set(stopwords.words('english'))
		tokenlist = [] 
	
		if type == "UserAnime":
			for string in desc_list:
				tokens = word_tokenize(str(string))
				
				for words in tokens:
					if words in stopset:
						tokens.remove(words)	
					
					elif words.isalpha() == False:
						tokens.remove(words)
					
					else:
						tokenlist.append(words)
			
			for words in tokenlist: 
				if words not in self.UserDesc:
					self.UserDesc[words] = 1
				else:
					self.UserDesc[words] += 1
		
		temp = {} 
		desc_dict = {} 
		if type == "GeneratedAnime":
			for key in desc_list.keys():
				description = desc_list[key]
				if description != 1:
					tokens = word_tokenize(str(description))
					for words in tokens:
						if words in stopset:
							tokens.remove(words)
						elif words.isalpha() == False:
							tokens.remove(words)
						else:
							tokenlist.append(words)
							temp[key] = tokenlist 
				else:
					temp[key] = 1
				
				tokenlist = [] 
			
			for id in temp.keys():
				tokenlist = temp[id]
				if tokenlist != 1:
					for words in tokenlist:
						if words not in desc_dict:
							desc_dict[words] = 1
						else:
							desc_dict[words] += 1
					self.GenDesc[id] = desc_dict
				else:
					self.GenDesc[id] = 1
				desc_dict = {}  
		
			
			
	def initCompany(self, comp_dict, type):
		c_dict = {} 
		#getting raw counts of each token 
		if type == "UserAnime": 
			for name in comp_dict:
				if name not in self.UserComp:
					self.UserComp[name] = 1 
				else:
					self.UserComp[name] += 1
			 
				
		if type == "GeneratedAnime": 
			for key in comp_dict.keys():
				c_list = comp_dict[key] 
				if c_list != 1: 
					for comp in c_list:
						if comp not in c_dict: 
							c_dict[comp] = 1
						else: 	
							c_dict[comp] += 1
					self.GenComp[key] = c_dict
					c_dict = {} 
				if c_list == 1:
					self.GenComp[key] = 1
	
	#havent developed a good implementation 
	def initRatings():
		pass
		
	def initGenres(self, genre_list, type):
		genre_dict = {} 
		if type == "GeneratedAnime":
			for key in genre_list.keys():
				g_list = genre_list[key] 
				for genres in g_list:
					if genres not in genre_dict: 
						genre_dict[genres] = 1
					else: 	
						genre_dict[genres] += 1
				self.GenGenre[key] = genre_dict
				genre_dict = {} 
		
		if type == "UserAnime": 
			for genre in genre_list: 
				if genre not in self.UserGenre:
					self.UserGenre[genre] = 1 
				else:
					self.UserGenre[genre] += 1

	def initStaff(self, staff_list, type):
		#getting raw counts of each token 
		staff_dict = {} 
		if type == "GeneratedAnime":
			for key in staff_list.keys():
				staff_array = staff_list[key]
				if len(staff_array) != 0: 
					for s in staff_array: 
						if s not in staff_dict:
							staff_dict[s] = 1
						else:	
							staff_dict[s] += 1
					self.GenStaff[key] = staff_dict
					staff_dict = {} 
				else:
					self.GenStaff[key] = 1 
						
		if type == "UserAnime": 
			for s in staff_list:
				if s not in self.UserStaff:
					self.UserStaff[s] = 1 
				else:
					self.UserStaff[s] += 1
					

	def TFIDF(self, user_dict, gen_dict, type):
		total_dict = {} 
		type_dict = {} 
		total_type_dict = {} 
		temp = {} 
		Return_Dict = {} 
		
		for key in user_dict.keys():
			if key not in total_dict:
				total_dict[key] = 1
			else:
				total_dict[key] += 1
				
		for key in gen_dict.keys():
			g_dict = gen_dict[key]
			if g_dict != 1:
				for word in g_dict.keys():
					if word not in temp:
						temp[word] = 1 
					else:
						temp[word] += 1
				total_type_dict[key] = temp 
				temp = {} 
			if g_dict == 1:
				total_type_dict[key] = 1
		
		# had to do this, for loop above was duplicating items when i initialized temp to genre_dict
		for key in total_type_dict.keys():
			dict = total_type_dict[key] 
			if dict != 1:
				for word in total_dict.keys():
					if word not in dict:
						dict[word] = 1
					else:
						dict[word] += 1 
				total_type_dict[key] = dict 
			if dict == 1: 
				total_type_dict[key] = 1
		
		for anime in total_type_dict.keys():
			g_list = total_type_dict[anime] 
			curr_list = gen_dict[anime]
			if curr_list != 1:
				for words in curr_list: 
					tf_all = g_list[words]
					div = 2/float(tf_all)
					idf_val = abs(log((div),10))
					tf_curr = 1+abs(log(curr_list[words],10))
					tf_idf = tf_curr * idf_val
					curr_list[words] = tf_idf 
				Return_Dict[anime] = curr_list 
			if curr_list == 1:
				Return_Dict[anime] = 1 
		
		print "\nTF IDF Scores for Generated: " + type, "\n"
		for key in Return_Dict.keys():
			print key, Return_Dict[key]
		
		return Return_Dict
						
				
			
if __name__ == "__main__":

	rec = Recommender() 
	file = "Output.json"
	Animelist = rec.read_json_file(file)
	UserList = rec.initUserAnime(Animelist)
	GenList = rec.initGenAnime(Animelist)
	rec.TFIDF(rec.UserDesc, rec.GenDesc, "Description")
	rec.TFIDF(rec.UserGenre, rec.GenGenre, "Genres")
	rec.TFIDF(rec.UserStaff, rec.GenStaff, "Staff")
	rec.TFIDF(rec.UserComp, rec.GenComp, "Companies")
	
	
	