import spacy

nlp = spacy.load('en')

to_process = input('enter some string: ')

doc = nlp(to_process)

words = []

for token in doc:
    pair = (token.text, token.pos_)
    words.append(pair)


for x in words: 
	print(x)