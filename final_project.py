from flask import Flask
from flask import redirect, url_for
from flask import request, make_response, Response
from flask import send_from_directory, jsonify
import json
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.form.get("addRow"):
        pass cuz idk what im doing

@app.route('/')
def classes():
    all_classes = get_data_from_db("select code, name from classes;")
    

if __name__ == '__main__':
    app.run()