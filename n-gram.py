import nltk
import re
import collections


data = open("sdata.txt", 'r').read()
filterOne = ''.join(filter(lambda x: not x.isdigit(), data))
filterTwo = (re.sub('[@#*()]', "", filterOne))
filterThree = (filterTwo.replace("SCENE", " "))
filterFour = (filterThree.replace("ACT", " "))
finalData = filterFour
'''
def format_sentence(sent):
    return {word: True for word in nltk.word_tokenize(sent)}


seg = []
with open("sdata.txt") as p:
    for words in p:
        seg.append([format_sentence(words), 'seg'])
'''
tokens = nltk.word_tokenize(finalData)
bigram = nltk.ngrams(tokens, 2)
print(collections.Counter(bigram))







