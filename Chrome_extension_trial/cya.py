import spacy

print "Content-type: text/html\n"

qs = os.environ['QUERY_STRING']
name = qs

nlp = spacy.load('en')

#to_process = input('enter some string: ')
to_process = name

doc = nlp(to_process)

for token in doc:
    #print(token.text, token.pos_)
    print "<html>"
    print "<body>"
    print(token.text, token.pos_)
    print "</pre>"
    print "</body>"
    print "</html>"
