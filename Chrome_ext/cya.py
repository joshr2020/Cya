import spacy
import json
import numpy

def process(to_process):
    nlp = spacy.load('en')

    doc = nlp(to_process)

    return doc[0].pos_
