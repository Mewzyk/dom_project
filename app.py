from flask import Flask
from flask import render_template
import requests
import json

app = Flask("getRoutey")

@app.route('/')
def hello():
    return render_template('index.html')
   
@app.route('/home') 
def home():
   return "home!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')



