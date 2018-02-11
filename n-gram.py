import nltk
from nltk.corpus import reuters


reuters


def format_sentence(sent):
     return {word: True for word in nltk.word_tokenize(sent)}


corpus = []
with open("reuters-corpus") as p:
      for words in p:
          corpus.append([format_sentence(words), 'corpus'])

