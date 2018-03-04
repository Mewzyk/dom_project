from flask import Flask
from flask import render_template
import requests
import json

app = Flask("getRoutey")

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/check_data')
def check():
    r = requests.get('https://www.mountainproject.com/data/get-routes-for-lat-lon?lat=36.5&lon=-121.202&maxDistance=10&minDiff=5.6&maxDiff=5.8&key=200212432-f3aa9be57f04ce46760dce00bef02b2d')
    database = r.json()
    routes = database['routes']
    object_keys = routes[0].keys()

    return '  '.join(object_keys)

   
@app.route('/home') 
def home():
    r = requests.get('https://www.mountainproject.com/data/get-routes-for-lat-lon?lat=36.5&lon=-121.202&maxDistance=10&minDiff=5.6&maxDiff=5.8&key=200212432-f3aa9be57f04ce46760dce00bef02b2d')
    database = r.json()
    routes = database['routes']

    print(routes[0]['id'])
    d = {}
    for route in routes:
        
        d[route['id']] = route

    with open('routeInfo.json', 'w') as outfile:
            json.dump(d, outfile)

    return "home!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')



