import spacy
import json


#loads and tolkenizes
nlp = spacy.load('en')

to_process = input('enter some string: ')

doc = nlp(to_process)

words = []

for token in doc:
    pair = (token.text, token.pos_)
    words.append(pair)

for x in words: 
	print(x)

#loads JSON into array
data = json.load(open('keywords.json'))


nounList = data['nouns']
adjList = data['adjective']

print(nounList)

	