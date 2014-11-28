#!/usr/bin/python

import cgi, cgitb
import os 
cgitb.enable()  # for troubleshooting

#the cgi library gets vars from html
data = cgi.FieldStorage()
#this is the actual output
print "Content-Type: text/html\n"
print "User Animelist: " + data["UserAnime"].value
data["RetrievedAnime"]=(os.popen('php ./php/pull.php').readline())
print "User RetrievedAnime: " +data["RetrievedAnime"]
"""
	fo = open("output.txt", "rw+")
	fo.seek(0)
	fo.truncate()

	UserAnime = "UserAnime"
	GenAnime = "GeneratedAnime" 
	str = data["UserAnime"].value
	# Write a line at the end of the file.
	fo.seek(0, 2)
	line = fo.write(UserAnime)
	line = fo.write( " " + str )
	str = data["RetrievedAnime"].value
	fo.seek(0, 2)
	line = fo.write("\n")
	line = fo.write(GenAnime)
	line = fo.write( " " + str )
"""
