
from nltk.corpus import reuters
from nltk import bigrams, trigrams
from collections import Counter, defaultdict

i_counter = Counter(reuters.words())
t_count = len(reuters.words())

print(i_counter.most_common(n=10))

for word in i_counter:
    i_counter[word]/= int(t_count)

    print(sum(i_counter.values()))

    import random

    text_rand = []

    for _ in range(100):
        r = random.random()
        counter_rand = .0

        for word, freq in i_counter.items():
            counter_rand += freq

            if counter_rand > r:
                text_rand.append(word)
                break
print(' '.join(text_rand))