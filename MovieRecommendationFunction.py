import json
import requests
from random import randint
##tt0076759

genre= raw_input("What genre: ")
minRating = raw_input("What is the lowest rating?")
#mediaType = raw_input("Movie or tv?")
KEY = '007d7263d6c65904a9285e1a3754a64c'


genreurl = "https://api.themoviedb.org/3/genre/movie/list?api_key=007d7263d6c65904a9285e1a3754a64c&query="
r = requests.get(genreurl)

genres= r.json()
for i in range(0,len(genres["genres"])-1):
     if (genres["genres"][i]["name"] == genre):
         genreID = genres["genres"][i]["id"]
         

###Finds a random movie that meets criteria.
movieurl = "https://api.themoviedb.org/3/genre/"+str(genreID)+"/movies?api_key=007d7263d6c65904a9285e1a3754a64c&query="
r = requests.get(movieurl)
res = r.json()   
for i in range(0,len(res["results"])):
    num = randint(0,len(res["results"])-1)
    if (res["results"][num]["vote_average"] >= float(minRating)):
        print "Title: " + res["results"][num]["original_title"]
        print "Overview: " + res["results"][num]["overview"]
        break

##if (res["results"][randint(0,len(res)-1)]["
##
##
##ID = res["results"][randint(0,len(res)-1)]["id"]
##movieurl = "https://api.themoviedb.org/3/movie/" + str(ID)+"?api_key=007d7263d6c65904a9285e1a3754a64c&query="
####
##r = requests.get(movieurl)
##res = r.json()
##
##print "Title: " + res["original_title"]
#print len(res["results"])


