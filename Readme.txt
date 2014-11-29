CSCE-470 Project 

Anime Recommender that will recommend user new anime seasons 
Currently using:
	MongoDB
	Phython
	Bootstrap html/js/css
Algorithm Check Point:

To test the execution of this code you will need the following files: ParseData.py & Output.json 
Output.json's contents were generated through API calls to gather animes with upcoming seasons and to gather the users anime watch list 
The user's anime watch list that was retrieved for this check point was from myanimelist.net user av512 (Alejandro Vega's account) 

To run the code, you may need to download nltk, to dowload it, do the following: 

Instructions taken from: http://blog.adlegant.com/how-to-install-nltk-corporastopwords/
 
	Type python so you access to the IDLE
	Type import nltk
	Type nltk.download() and you will enter into the NLTK Downloader manager. It allows you to add language packages to your NLTK library 
	You need to type d or Download
	The downloader manager will ask you to give a package identifier so type all-corpora or type l to see all packages available
	Enter and your download will start
	
from the terminal enter
> python ParseData.py  > outputfile 

When you open the outputfile, outputs that you will see consist of tf idf scores of descriptions of generated anime, genre, companies, staff. 

The file Parse Data Output contains the outputs for the ParseData.py script 

At this stage, the code only calculated tf idf scores will use cosine. Additionally the output score previously mentioned will be multiplied by a given
alpha value and added together to get a better approximation for the users anime preferences 


http://learn.koding.com/guides/install-mongodb/

http://api.mongodb.org/python/current/installation.html

to populate your datbase you must run your mongodb server
and then open in your browser the retrieveData.html in your browser and don't recieve an error

pip install -U textblob nltk
python -m textblob.download_corpora

