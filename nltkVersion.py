import nltk
from nltk import word_tokenize, sent_tokenize
from nltk import bigrams, trigrams
from collections import Counter, defaultdict
from operator import mul

import re

data = open("westPhil.txt", 'r').read()
fTwo = (re.sub(',[0-9\W]+', " ", data))
fThree = (fTwo.replace("SCENE", " "))
fFour = (fThree.replace("ACT", " "))
final_data = fFour
tokens = word_tokenize(final_data)
tokens_final = [item.lower() for item in tokens]
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

print(reduce(mul, [i_counter[w] for w in text_rand], 1.0))

bigram_sentence = nltk.ngrams(tokens_final, 2, pad_left=True, pad_right=True)

print(bigram_sentence)

lm_model = defaultdict(lambda: defaultdict(lambda: 0))

for w1, w2 in bigram_sentence:
    lm_model[w1][w2] += 1


for w1 in lm_model:
    # was using int, but for now obvious reasons had to switch to float
    t_count = float(sum(lm_model[w1].values()))
    # actually getting probabilities, with bigrams
    for w2 in lm_model[w1]:
        lm_model[w1][w2] /= t_count

# tests: passed
print(lm_model["view"]["would"])
print(lm_model["than"]["mathematical"])
# test:passed
print(lm_model[None]["aff"])
