import nltk
from nltk.probability import *
import re
import collections

data = open("sdata.txt", 'r').read()
fOne = ''.join(filter(lambda x: not x.isdigit(), data))
fTwo = (re.sub('[@#*%;()}]', "", fOne))
fThree = (fTwo.replace("SCENE", " "))
fFour = (fThree.replace("ACT", " "))
finalData = fFour
tokens = nltk.word_tokenize(finalData)
bigram = nltk.ngrams(tokens, 2)
collections.Counter(bigram)
trigram = nltk.ngrams(tokens, 3)
collections.Counter(trigram)

total = 0
count = collections.defaultdict(int)
for word in finalData:
    total += 1
    count[word] += 1
for word, ct in count.items():
     print([word, 100.0 * int(ct) / int(total)])






