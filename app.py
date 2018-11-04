from flask import Flask
from histogram import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    print(frequency(unique_words("text-corpus.txt"),read_sterilize_source("text-corpus.txt")))
    return "ello, gov'na!"
