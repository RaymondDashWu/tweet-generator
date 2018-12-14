import cleanup
import tokenize
import word_count
from sample import *
# import sample
import sentence

from flask import Flask
from histogram import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return sample

if __name__ == "__main__":
    corpus = read_sterilize_source("sarcasm.txt")
    chain = markov_chain_nth_order(corpus)
    sentence_list = markov_chain_walk(chain)
    print('sentence_list:', sentence_list)
    
    
    
    # with open("text-corpus.txt", "r") as file:
    #     source = file.read()
    # # removes symbols, punctuation, etc. from source text and puts in array
    # sterilized_source = read_sterilize_source(source)
    # # retrieves uniques from above sterilized source
    # sterilized_source_uniques = unique_words(sterilized_source)
    # # counts the instances of uniques in sterilized source text
    # sterilized_source_frequency = frequency(sterilized_source_uniques, sterilized_source)
