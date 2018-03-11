from nltk import word_tokenize
from nltk import bigrams, trigrams
from collections import Counter, defaultdict


import re
data = open("sdata.txt", 'r').read()
fTwo = (re.sub('[0-9\W]+', " ", data))
fThree = (fTwo.replace("SCENE", " "))
fFour = (fThree.replace("ACT", " "))
final_data = fFour
tokens = word_tokenize(final_data)
tokens_final =[item.lower() for item in tokens]
i_counter = Counter(tokens_final)
t_count = len(tokens_final)


for word in i_counter:
    i_counter[word] /= float(t_count)

    print(sum(i_counter.values()))

    import random
    from functools import reduce

text_rand = []

for _ in range(10):
        r = random.random()
        counter_rand = .0

        for word, freq in (i_counter.items()):
            counter_rand += freq

            if counter_rand > r:
                text_rand.append(word)
                break

print(' '.join(text_rand))


from operator import mul
print(reduce(mul, [i_counter[w] for w in text_rand], 1.0))
