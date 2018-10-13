





### Goals
###### 1. Tokenize and sentence-segment corpus. This can be done by either
###### writing regular expressions or using => [NLTK](http://www.nltk.org).
###### 2. Compute a smoothed language model. It should at least use one previous
###### word, i.e. it will be a bi-gram language model. 
###### 3. Evaluate your language model informally. E.g. compute the probability
###### of a sentence in a different language (e.g. Spanish) and convince yourself
###### that it’s much lower than the probability of an English sentence.
###### Also compare the probabilities of a well-formed and a malformed English
###### sentence (e.g. All your base are belong to us). 
###### 4. Evaluate language model by computing the perplexities of two text
###### documents: one should come from the same domain as the corpus on which
###### the trained model comes from. The other one should come from a completely
###### different domain. E.g. if the language model was trained on the Reuters
###### corpus, you can compare the perplexities for an article appearing on CNN
###### vs. a few pages from Shakespeare. Comment on the differences in perplexity.

#### N-Grams 
* ["In the fields of computational linguistics and probability, an n-gram is a 
contiguous sequence of n items from a given sample of text or speech. The items 
can be phonemes, syllables, letters, words or base pairs according to the application.
 The n-grams typically are collected from a text or speech corpus"](https://en.wikipedia.org/wiki/N-gram)


#### how to use + generate random sentence



#### NLTK IS AWESOME!!!
* you can import the entire reuters corpus, without having to parse it all, simply:
```python
import nltk
from nltk.corpus import reuters

```

* check out this article => [reuters-corpus](https://miguelmalvarez.com/2015/03/20/classifying-reuters-21578-collection-with-python-representing-the-data/)

* more on the => [corpus' from nltk](http://www.nltk.org/howto/corpus.html)
