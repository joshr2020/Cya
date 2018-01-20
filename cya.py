import spacy
import json

nlp = spacy.load('en')

to_process = input('enter some string: ')

doc = nlp(to_process)

words = []

for token in doc:
    pair = (token.text, token.pos_)
    words.append(pair)


for x in words: 
	print(x)

data = json.load(open('keywords.json'))



#loads the json keywords file into a dict
for key, value in data.items():
		for k, v in value.items():
			print(k)