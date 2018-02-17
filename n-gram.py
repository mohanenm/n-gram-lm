import nltk
from nltk.probability import *
import re
import collections
from collections import Counter

''' cleaning data'''
data = open("sdata.txt", 'r').read()
fOne = ''.join(filter(lambda x: not x.isdigit(), data))
fTwo = (re.sub('[-,_[@#*?!.""%;()}]', " ", fOne))
fThree = (fTwo.replace("SCENE", " "))
fFour = (fThree.replace("ACT", " "))
finalData = fFour

'''tokenization + nltk bigram,trigram generation 

tokens = nltk.word_tokenize(finalData)
bigram = nltk.ngrams(tokens, 2)
Counter(bigram)
trigram = nltk.ngrams(tokens, 3)
Counter(trigram)

'''

wordcount = Counter(finalData.split())
for item in wordcount.items():
    print("{}\t{}".format(*item))

print(len(finalData.split()))





