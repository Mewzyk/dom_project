from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def hello():
    
   # r = request.get('https://www.mountainproject.com/data/get-routes-for-lat-lon?lat=36.5&lon=-121.202&maxDistance=10&minDiff=5.6&maxDiff=5.8&key=200212432-f3aa9be57f04ce46760dce00bef02b2d')
    #database = r.json()
    #routes = database['routes']
    #print(routes)

    return ('hello')
    

if __name__ == '__main__':
    app.run(host='0.0.0.0')
