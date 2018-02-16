
 import collections
 import nltk
 from nltk.corpus import reuters




def format_sentence(sent):
     return {word: True for word in nltk.word_tokenize(sent)}


def collection_stats():
    # List of documents
    documents = reuters.fileids()
    print(str(len(documents)) + " documents");

    id = category_docs[0]
    words =

with read(id) a:
      for words in p:
          corpus.append([format_sentence(words), 'corpus'])



l = [corpus]

collections.counter(l)

