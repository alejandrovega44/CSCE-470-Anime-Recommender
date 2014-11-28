#!/usr/bin/python

import cgi, cgitb
import os 
from functions import Functions
cgitb.enable()  # for troubleshooting

#the cgi library gets vars from html
data = cgi.FieldStorage()
#this is the actual output
debug = True
writeFile = False
print "Content-Type: text/html\n"
if not debug:
    print "User Animelist: " + data["UserAnime"].value
temp=(os.popen('php ./../php/pull.php').readline())
 
if debug and writeFile:
    U_f = open('./UserAnime', 'w')
    U_f.write(data["UserAnime"].value)
    U_f.close()
    R_f= open('./RetrievedAnime','w')
    R_f.write(temp)
    R_f.close()
elif debug and not writeFile:
    U_f=open('./UserAnime', 'r')
    line=U_f.read()
    R_f=open('./RetrievedAnime','r')
    line2=R_f.read()

line = Functions.read_line(line)
line2 = Functions.read_line(line2)
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
