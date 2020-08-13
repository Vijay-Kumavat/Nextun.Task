# -*- coding: utf-8 -*-
# """
# Spyder Editor

# This is a temporary script file.
# """



"""
token = 'EAAIxTzg7G6kBAALPIDNYn05pzEOOtTgCadWh01tX0ClIMpCjMYKaRJKYN6uyjk0JPK0Y8cRJXNLibJTPAqAy4cd86t7m7MhJ2CyTCKisFput3ItERQM6DRHqBsnhdOoPtZCyv1a5I5ZAG9xWZA31ZCgcFscpjqjoQTHxh2E66bihZC8QHnuG3SPkD19c9uXxMuNNFZCMWd5gZDZD'


appid = 'https://graph.facebook.com/v8.0/appid?access_token='+token

import requests

appid1=requests.get(appid)
"""


token = 'EAAkEUMmXLVUBAFKsS2vsbtKaNNHCQgOJyELdviOFvRmkzguHZCAfM1tPBnuQLQneZC5zSk7KuHrehX3xnDZBH99fvZC5BZBImXrFJVEVwkbHRGGwkK6jRSsmzirQEDJ9BL8aZBvbjeEUb6gZB6KvVFPeH05n0YXekCza9pFGUg6YX39uWyZA5CJR0f5ecfauYidJyImJsCz6Jhwi4W8dEKzgE4bZAN8Oizbqvg6iumPowWAZDZD'
#
me = 'https://graph.facebook.com/v8.0/me?access_token='+token
#
friends = 'https://graph.facebook.com/v8.0/me/friends?access_token='+token
#
search = 'https://graph.facebook.com/v8.0/search?q=mark zukerberg&type=user&access_token='+token
#
import requests
#
me1=requests.get(me)

f1 = requests.get(friends)

s1 = requests.get(search)




#import json
#import facebook

#def main():
    #token = {
     #   'EAAkEUMmXLVUBAB0GDGgZCEj3vgnUQDqhZBj1mPwVJBrn2ZC4rSOiZBoLuRcNF3CTPzUhUoYsg5LVqyPl7XP0hK1NQnmPvp7vKRTrvRJcY50ePJZCwAW439RumIvP3ZBSuqUdg7HTql1iJnanBZC9kxycBbrO3arGNzpucDwLgPUBdeXPpZB9r5sbytpV4NREWKZCZCct2ImqdMWGPOv4wU1HoD4jA6NabMZBDBgt6pCRq36tAZDZD'}
    #graph = facebook.GraphAPI(token)

    #fields = ['App ID,Page ID,Issued,Data Acess Expires,Origin']

   # profile = graph.get_object('me', fields=fields)

  #  print(json.dump(profile, indent=4))


#if __name__ == "__main__":
 #   main()
