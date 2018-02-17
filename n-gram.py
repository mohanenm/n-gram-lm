import nltk
import collections


textData = open("sdata.txt").read()


'''
tokens = nltk.word_tokenize(textData)
def format_sentence(sent):
    return {word: True for word in nltk.word_tokenize(sent)}


seg = []
with open("sdata.txt") as p:
    for words in p:
        seg.append([format_sentence(words), 'seg'])
'''



tokens = nltk.word_tokenize(textData)
bigram = nltk.ngrams(tokens, 2)
print(collections.Counter(bigram))







