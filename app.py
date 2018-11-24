import cleanup
import tokenize
import word_count
import sample
import sentence

from flask import Flask
from histogram import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    for _ in range(0,10):
        return random.choice(unique_words(read_sterilize_source("text-corpus.txt")))

if __name__ == "__main__":
    with open("text-corpus.txt", "r") as file:
        source = file.read()
    # removes symbols, punctuation, etc. from source text and puts in array
    sterilized_source = read_sterilize_source(source)
    # retrieves uniques from above sterilized source
    sterilized_source_uniques = unique_words(sterilized_source)
    # counts the instances of uniques in sterilized source text
    sterilized_source_frequency = frequency(sterilized_source_uniques, sterilized_source)
