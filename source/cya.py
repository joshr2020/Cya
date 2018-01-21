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
def adjFindPerStatement(list):
	matchString = ""
	for row in list:
		if row[1] == 'ADJ' or row[1] == 'PUNCT':
			matchString += str(row[0])
	return matchString

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
	input_adj_string = adjFindPerStatement(inputSet)
	input_adj = input_adj_string.split(".")


	noun_matches = []

	#loops through nouns to see if there is match
	for noun in input_nouns:
		 if findWordDict(nounDataBase, noun) == 1:
		 	noun_matches.append(noun)
	adj_matches = []

	#loops through adj to see if there is match
	for adj in input_adj:
		 if findWordDict(adjDataBase, adj) == 1:
		 	adj_matches.append(adj)

	return noun_matches, adj_matches

def calculate_score(data, noun_matches, adj_matches):
	total_score = 0
	for i in range(0, len(noun_matches)):
		a_score = 0
		if data['nouns'][noun_matches[i]]['type'] is 'trigger':
			a_score = data['nouns'][noun_matches[i]]['score'] * 3
		elif data['nouns'][noun_matches[i]]['type'] is not data['adjective'][adj_matches[i]]['type']:
			a_score = 2 * (data['nouns'][noun_matches[i]]['score'] + data['adjective'][adj_matches[i]]['score'])
		else:
			a_score = data['nouns'][noun_matches[i]]['score'] + data['adjective'][adj_matches[i]]['score']
		total_score = total_score + int(a_score)
	return total_score / len(noun_matches)


def get_result(score):
	responses = ["There are no nouns that are relavent in this post, please try again",
	"This message will cause no aggressive feedback or controversy",
	"There may be some controversial topics here. Be prepared for a discussion",
	"This statment is divisve and might provoke a strong response from others.",
	"This is a highly controversial post. Be prepared to spend a lot of time fending off aggressive comments."]

	if score == -1:
		return responses[0]
	elif 0 <= score and score < 7:
		return responses[1]
	elif 7 <= score and score < 15:
		return responses[2]
	elif 15<= score and score < 22:
		return responses[3]
	else:
		return responses[4]
	


def process(to_process):
	#loads and tolkenizes
	nlp = spacy.load('en')

	doc = nlp(to_process)

	noun_adj_pair = doc.noun_chunks

	words = []

	for token in doc:
		row = [str(token.text), str(token.pos_)]
		words.append(row)

	#loads JSON into array
	data = json.load(open('keywords.json'))

	#Finds Matching nouns and adj
	noun_matches, adj_matches = matchWords(data, words)

	#The edge cases
	if len(noun_matches) == 0:
		score = -1
		result = get_result(score)
		return result
	if len(adj_matches) == 0:
		total = 0
		for i in range(0, len(noun_matches)):
			part_score = data['nouns'][noun_matches[i]]['score']
			total = total + int(part_score)
		score = total/len(noun_matches)
		result = get_result(score)
		return result

	score = calculate_score(data, noun_matches, adj_matches)
	result = get_result(score)
	return result
