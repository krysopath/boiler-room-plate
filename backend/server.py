#!/usr/bin/env python3
from flask import Flask
from sys import argv
import os

app = Flask(__name__)

BIND = argv[1]
PORT= argv[2]

@app.route("/")
def bait(): 
    return app.send_static_file('index.html')

if __name__ == "__main__":  
    app.run(host=BIND,port=PORT,debug=True)

