import re
from collections import Counter
import nltk
from nltk import sent_tokenize, word_tokenize
from nltk import ngrams
from nltk import FreqDist
import itertools

''
'cleaning data'
''
data = open("sdata.txt", 'r').read()
fTwo = (re.sub('[0-9\W]+', " ", data))
fThree = (fTwo.replace("SCENE", " "))
fFour = (fThree.replace("ACT", " "))
finalData = fFour
''' 
  tokenization + nltk bigram,trigram generation 

'''
tokens = word_tokenize(finalData)
wordcount = Counter(finalData.split())
for item in wordcount.items():
   ("{}\t{}".format(*item))
totalWordcount = sum(wordcount.values())
''
'total word count: 963989'
''
''
' sentence segmenting'
''
sent_tokenize_list = sent_tokenize(finalData)
print(sent_tokenize)
bigram = list(nltk.bigrams(finalData.split()))
print(*map(' '.join, bigram), sep=',')
wordCounter = Counter(bigram)
for k,v in wordCounter.items():
    final = v/totalWordcount

    print(final)


