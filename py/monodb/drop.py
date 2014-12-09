from pymongo import MongoClient

client = MongoClient()
db = client.UpcomingAnime
collection_Anime=db.Anime
collection_Anime.drop()
