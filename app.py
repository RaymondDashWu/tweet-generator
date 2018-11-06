from flask import Flask
from histogram import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return random.choice(unique_words("text-corpus.txt"))
    return "ello, gov'na!"
