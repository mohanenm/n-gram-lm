from nltk import word_tokenize
from nltk import bigrams, trigrams
from collections import Counter, defaultdict


import re

'''
data = open("sdata.txt", 'r').read()
fTwo = (re.sub('[0-9\W]+', " ", data))
fThree = (fTwo.replace("SCENE", " "))
fFour = (fThree.replace("ACT", " "))
finalData = fFour
'''

tokens = word_tokenize(finalData)

i_counter = Counter(finalData.words())
t_count = len(finalData.words())


for word in i_counter:
    i_counter[word] /= float(t_count)

    print(sum(i_counter.values()))

    import random

text_rand = []

for _ in range(100):
        r = random.random()
        counter_rand = .0

        for word, freq in (i_counter.items()):
            counter_rand += freq

            if counter_rand > r:
                text_rand.append(word)
                break

print(' '.join(text_rand))


from operator import mul
print(reduce(mul, [counts[w] for w in text], 1.0))
