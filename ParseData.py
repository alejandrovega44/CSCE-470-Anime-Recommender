import json,ast #or cjson
from math import log,sqrt
import re

class Recommender(object):
	def __init__(self):
	
		self.UserStaff = []
		self.GenStaff = []
		
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
		
		User = Animelist[0]
		Gen = Animelist[1] 
		UserAnimes = User[1]
		GenAnimes = Gen[1] 
		
		ani_desc = [] 
		ani_staff = [] 
		ani_genres = [] 
		ani_staff = []
		
		g_desc = [] 
		g_staff = [] 
		g_genres = [] 
		g_staff = []
			
		for anime, dict in UserAnimes.items():
			
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
					# if item not in ani_genres:
						# ani_genres.append(item)
						# print item 
	
			#need to pair user ratings with genres 
			
		for g_anime, g_dict in GenAnimes.items():
			
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

					
	def getAnimeDes():
		pass 
		
	def getRatings():
		pass

	def getStaff():
		pass 
	

			
if __name__ == "__main__":

	rec = Recommender() 
	file = "RecOutput.json"
	Animelist = rec.read_json_file(file)
	parseAnimes = rec.init(Animelist)
	
	
	