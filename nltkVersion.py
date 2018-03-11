import nltk
from nltk import word_tokenize, sent_tokenize
from nltk import bigrams, trigrams
from collections import Counter, defaultdict
from operator import mul
import random
import re

# ideas for dictionary, bag of words ==> actual model came from http://nlpforhackers.io/language-models/ + nltk documentation(excessively)

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

print(reduce(mul, [i_counter[a] for a in text_rand], 1.0))


# bi-gram generatioon + bi-gram

bigram_sentence = nltk.ngrams(tokens_final, 2, pad_left=True, pad_right=True)
trigram_sentence = nltk.ngrams(tokens_final, 3, pad_left=True, pad_right=True)
print(bigram_sentence)
print(trigram_sentence)
lm_model = defaultdict(lambda: defaultdict(lambda: 0))

for a1, a2 in bigram_sentence:
    lm_model[a1][a2] += 1

for a1 in lm_model:
    # was using int, but for now obvious reasons had to switch to float
    t_count = float(sum(lm_model[a1].values()))
    # actually getting probabilities, with bigrams
    for a2 in lm_model[a1]:
        lm_model[a1][a2] /= t_count

# tests: passed
print(lm_model["view"]["would"])
print(lm_model["than"]["mathematical"])
# test:passed:0, naturally
print(lm_model[None]["aff"])


text = [None, None]
prob = 1.0
sentence_finished = False

while not sentence_finished:
    r = random.random()
    counter_rand2 = .0
    for word in lm_model[tuple(text[-2:])].keys():
        counter_rand2 += lm_model[tuple(text[-2:])][word]
        if counter_rand2 >= r:
            prob *= lm_model[tuple(text[-2:])][word]
            print(prob)
            text.append(word)
            break
    if text[-2:] == [None, None]:
        sentence_finished = True

print("Probability of text=", prob)
print(' '.join([t for t in text if t]))









model = defaultdict(lambda: defaultdict(lambda: 0))

for a1, a2, a3 in trigram_sentence:
        model[(a1, a2)][a3] += 1

print(model["according", "to"]["this"])
print(model["what", "the"]["nonexistingword"])
print(model[None, None]["The"])


for a1_a2 in model:
    total_count = float(sum(model[a1_a2].values()))
    for a3 in model[a1_a2]:
        model[a1_a2][a3] /= total_count

text = [None, None]

sentence_finished = False

while not sentence_finished:
    r = random.random()
    tri_counter = .0
    for word in model[tuple(text[-2:])].keys():
        tri_counter += model[tuple(text[-2:])][word]
        if tri_counter >= r:
            text.append(word)
            break
    if text[-2:] == [None, None]:
        sentence_finished = True

print(' '.join([t for t in text if t]))






'''

# six-gram generatioon + tri-gram
sixgram_sentence = nltk.ngrams(tokens_final, 6, pad_left=True, pad_right=True)
print(sixgram_sentence)


lm_six_model = defaultdict(lambda: defaultdict(lambda: 0))
for b1, b2, b3, b4, b5, b6  in sixgram_sentence:
    lm_six_model[b1][b2][b3][b4][b5][b6] += 1

for b1 in lm_six_model:
    t_count = float(sum(lm_model[a1].values()))
    # actually getting probabilities, with bigrams
    for a2 in lm_model[a1]:
        lm_model[a1][a2] /= t_count
'''


