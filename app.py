from flask import Flask
from histogram import *
# from histogram import *
app = Flask(__name__)
 @app.route('/')
def hello_world():
    # print(frequency(unique_words("text-corpus.txt"),read_sterilize_source("text-corpus.txt")))
    # print(frequency(unique_words("text-corpus.txt"),read_sterilize_source("text-corpus.txt")))
    print("hello_world")
    return "ello, gov'na!"
