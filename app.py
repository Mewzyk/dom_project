from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo
import json

app = Flask("getRoutey")
app.config['MONGO_HOST'] = '18.219.228.163'
app.config['MONGO_PORT'] = 27017
app.config['MONGO_DBNAME'] = 'getRoutey'
mongo = PyMongo(app, config_prefix='MONGO')

@app.route('/')
def index():
    return render_template('index.html')
   
@app.route('/home') 
def home():
    return "home!"

@app.route('/get_route_data')
def get_route_data():
    print(mongo.db.getRoutey.find_one())
    return "Hello World"

if __name__ == '__main__':
    app.run(host='0.0.0.0')

