import spacy
import json

#loops through list
def nounfind(list):
	matches = []
	for row in list:

		if row[1] == 'PROPN' or row[1] == 'NOUN':
			matches.append(row[0])
	return matches

#loops through list
def adjfind(list):
	matches = []
	for row in list:

		if row[1] == 'ADJ':
			matches.append(row[0])
	return matches

#loops through dictionary
def findWordDict(input_dict, word):
	for key in input_dict.keys():
		if word == key:
			return 1
	return 0

def matchWords(data, inputSet):
	nounDataBase = data['nouns']
	adjDataBase  = data['adjective']

	#calls nouns to filter for nouns
	input_nouns = nounfind(inputSet)
	#print(input_nouns)
	#calls adj to filter for adjectives
	input_adj = adjfind(inputSet)

	#exits if no nouns exist
	if len(input_nouns) == 0:
		print("No nouns here match our database.")
		exit(0)

	noun_matches = []
	#loops through nouns to see if there is match
	for noun in input_nouns:
		 if findWordDict(nounDataBase, noun) == 1:
		 	noun_matches.append(noun)
	print(noun_matches)

	return 2


def process(to_process):
    #loads and tolkenizes
    nlp = spacy.load('en')

    doc = nlp(to_process)

    #print(doc.noun_chunks)

    words = []

    for token in doc:
        row = [str(token.text), str(token.pos_)]
        words.append(row)

    for x in words:
    	print(x)

    #loads JSON into array
    data = json.load(open('keywords.json'))

    #Finds Match
    return matchWords(data, words)
