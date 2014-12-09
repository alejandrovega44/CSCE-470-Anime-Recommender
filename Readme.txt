CSCE-470 Project 

Anime Recommender that will recommend user new anime seasons 
This uses content based recommendation with the use of NaiveBayes
returning the top 6 relevant animes to the user
the features currently used are:
genres and staff

Technologies Currently using:
	MongoDB
	Phython
	nltk
	Bootstrap html/js/css

install python

http://learn.koding.com/guides/install-mongodb/

http://api.mongodb.org/python/current/installation.html

to populate your datbase you must run your mongodb server
and then open in your browser the Pages/retrieveData.html in your browser and don't recieve an error, if do refresh
but first you must do the following: 

sudo apt-get install python-pip
pip install simplejson
pip install -U textblob nltk
python -m textblob.download_corpora

step 1:create nltk_data folder in  '/usr/lib/ 
step 2:move nltk_data folder to '/usr/lib/nltk_data'

if step 1 and step 2 don't work just make sure that the folder called nltk_data
downloaded from the pyton -m textblob.download_corpora is inside your web folder

Some users to test:

OHdamnnn
zum_bum
erick
ann
SweetKotomi
LightSpark090
SerasAshley
