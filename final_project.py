from flask import Flask
from flask import redirect, url_for
from flask import request, make_response, Response
from flask import send_from_directory, jsonify
import json
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    pass

if __name__ == '__main__':
    app.run()