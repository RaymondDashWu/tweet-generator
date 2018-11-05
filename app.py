from flask import Flask
# from histogram import *
app = Flask(__name__)

def gunicorn_app(environ, start_response):
        data = b"Hello, World!\n"
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])

@app.route('/')
def hello_world():
    # print(frequency(unique_words("text-corpus.txt"),read_sterilize_source("text-corpus.txt")))
    return "ello, gov'na!"
