
import re
from collections import Counter
import math
import nltk
from nltk.collocations import *
from nltk.probability import *
import sets

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
text = "I do not like green eggs and ham, I do not like them Sam I am!"

words = re.split('[^A-Za-z]+', text.lower())
unigram = set(words)
print(len(unigram))
print(unigram)

for i in range(len(words)-10, len(words)-1):
     print(words[i], words[i +1])

word_pairs = [(words[i], words[i+1]) for i in range(len(words)-1)]
print(len(word_pairs))

gram2 = set(word_pairs)
print(len(gram2))

unigram = dict()

for word in words:
    if unigram.has_key(word):
        unigram[word] += 1
    else:
        unigram[word] = 1

unigram = sorted(unigram.items(), key=star(lambda word, count: word*word + count*count) -count)










