from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo
import requests
import json

app = Flask("getRoutey")
mongo_instance = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')
   
@app.route('/home') 
def home():
    return "home!"

@app.route('/get_route_data')
def get_route_data():
    routes = mongo_instance.db.routes
    print(json.dumps(routes))
    return json.dumps(routes)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

