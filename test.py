import re
from collections import Counter
import math
import nltk
import random
from nltk.collocations import *
from nltk.probability import *
import sets

# this set utilizing version is not done

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
text = open('sdata.txt').read()

words = re.split('[^A-Za-z]+', text.lower())
unigram = set(words)
print(len(unigram))
print(unigram)

word_pairs = [(words[i], words[i + 1]) for i in range(len(words) - 1)]
print(len(word_pairs))

bigram = set(word_pairs)
print(len(bigram))

# Print 20 elements from gram2
bigram_iter = iter(bigram)
print([next(bigram_iter) for i in range(20)])

unigram = dict()

for word in words:
    if word in unigram:
        unigram[word] += 1
    else:
        unigram[word] = 1

unigram = sorted(unigram.items(), key=lambda word_count: word_count[1])

print(unigram[:20])

bigram = dict()

for i in range(len(words) - 1):
    key = (words[i], words[i + 1])
    if key in bigram:
        bigram[key] += 1
    else:
        bigram[key] = 1

bigram = sorted(bigram.items(), key=lambda __count: __count[1])

print(bigram[:20])

start_word = (random.choice(words))
print(start_word)


def get2gramsentence(word, n=50):
    for i in range(n):
        print(word),
        # Find Next word
        word = next((element[0][1] for element in bigram if element[0][0] == word), None)
        if not word:
            break


word = start_word
print("Start word: %s" % word)
print("2-gram sentence:", get2gramsentence(word, 10))
