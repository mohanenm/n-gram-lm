import re
from collections import Counter
import math
import nltk
from nltk import sent_tokenize, word_tokenize
from nltk import ngrams
from nltk import FreqDist
import itertools

sentenceStart = "<s>"
sentenceEnd = "</S>"
''
'cleaning data'
''

data = open("sdata.txt", 'r').read()
fTwo = (re.sub('[0-9\W]+', " ", data))
fThree = (fTwo.replace("SCENE", " "))
fFour = (fThree.replace("ACT", " "))
finalData = fFour
''
'tokenization + nltk bigram,trigram generation'
''

tokens = word_tokenize(finalData)
unigram = Counter(finalData.split())
for item in unigram.items():
  print("{}\t{}".format(*item))



  '''totalWordcount = sum(unigram.values())'''

'''
sent_tokenize_list = sent_tokenize(finalData)
token = sent_tokenize
bigram = list(nltk.bigrams(finalData.split()))
print(sep=',', *map(' '.join, bigram))
wordCounter = Counter(bigram)
for k, v in wordCounter.items():
    print(k, (v/988559))
'''


