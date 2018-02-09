





### Goals
#### From HW assignment in Comp 388 @loyolachicago
###### 1. Tokenize and sentence-segment corpus. This can be done by either
###### writing regular expressions or using NLTK (http://www.nltk.org).
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
