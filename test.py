import re
from collections import Counter
import math
import nltk
import nltk
from nltk.collocations import *
import nltk
from nltk.probability import *

sentenceStart = "<s>"
sentenceEnd = "</S>"

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
text = "I do not like green eggs and ham, I do not like them Sam I am!"
tokens = nltk.wordpunct_tokenize(text)
finder = BigramCollocationFinder.from_words(tokens)
scored = finder.score_ngrams(bigram_measures.raw_freq)
print(sorted(bigram for bigram, score in scored))
print(len(tokens))



