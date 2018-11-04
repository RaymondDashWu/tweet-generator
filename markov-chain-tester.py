import random
import sys

corpus = ["I", "you", "went", "left", "right"]

def make_pairs(corpus):
    for index in range(len(corpus) - 1):
        yield (corpus[i], corpus[i + 1])

def build_chain(word, chain = {}):
    for index in corpus:
