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
fOne = ''.join(filter(lambda x: not x.isdigit(), data))
fTwo = (re.sub('[-,_[@#*""%;()}]', " ", fOne))
fThree = (fTwo.replace("SCENE", " "))
fFour = (fThree.replace("ACT", " "))
finalData = fFour

''' 
  tokenization + nltk bigram,trigram generation 

'''

tokens = word_tokenize(finalData)
bigram = nltk.ngrams(tokens, 2)
print(bigram)

wordcount = Counter(finalData.split())
for item in wordcount.items():
    print("{}\t{}".format(*item))

''
'total word count: 963989'
''
print(len(finalData.split()))
''
' sentence segmenting'
''
sent_tokenize_list = sent_tokenize(finalData)
print(sent_tokenize)
bigram = ngrams(sent_tokenize(finalData), 2)
fdist = FreqDist(itertools.chain(bigram))
print(fdist)
