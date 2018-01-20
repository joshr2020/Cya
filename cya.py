import spacy

nlp = spacy.load('en')

to_process = input('enter some string: ')

doc = nlp(to_process)

for token in doc:
    print(token.text, token.pos_)
