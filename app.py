import cleanup
import tokenize
import word_count
from sample import markov_chain_walk, markov_chain_nth_order
 # import sample
import sentence
from histogram import read_sterilize_source
 
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    corpus = read_sterilize_source("sarcasm.txt")
    chain = markov_chain_nth_order(corpus)
    sentence_list = markov_chain_walk(chain)
    print('sentence_list:', sentence_list)

if __name__ == "__main__":
    hello_world.run()
     
     
     
     # with open("text-corpus.txt", "r") as file:
     #     source = file.read()
     # # removes symbols, punctuation, etc. from source text and puts in array
     # sterilized_source = read_sterilize_source(source)
     # # retrieves uniques from above sterilized source
     # sterilized_source_uniques = unique_words(sterilized_source)
     # # counts the instances of uniques in sterilized source text
     # sterilized_source_frequency = frequency(sterilized_source_uniques, sterilized_source)



# from flask import Flask
# from histogram import *
# # from histogram import *
# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     # print(frequency(unique_words("text-corpus.txt"),read_sterilize_source("text-corpus.txt")))
#     # print(frequency(unique_words("text-corpus.txt"),read_sterilize_source("text-corpus.txt")))
#     print("hello_world")
#     return "ello, gov'na!"
