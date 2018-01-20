from textblob import TextBlob
#import requests
#import nltk

post = input("Please type your post here: ")

blob = TextBlob(post)

x = blob.noun_phrases