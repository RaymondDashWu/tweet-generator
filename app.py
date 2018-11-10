from flask import Flask
from histogram import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    for _ in range(0,10):
        return random.choice(unique_words(read_sterilize_source("text-corpus.txt")))

print(hello_world())