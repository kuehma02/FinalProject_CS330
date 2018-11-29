from flask import Flask
from flask import redirect, url_for
from flask import request, make_response, Response
from flask import send_from_directory, jsonify
from flask import render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.form.get("addRow"):
        pass

@app.route('/classes')
def classes():
    all_classes = get_data_from_db("select code, name from classes;")
    

if __name__ == '__main__':
    app.run()