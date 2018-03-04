import json
import pprint
import requests
from pymongo import MongoClient

client = MongoClient()
collection = client.getRoutey.routes


r = requests.get('https://www.mountainproject.com/data/get-routes-for-lat-lon?lat=36.5&lon=-121.202&maxDistance=10&minDiff=5.6&maxDiff=5.8&key=200212432-f3aa9be57f04ce46760dce00bef02b2d')
database = r.json()
routes = database['routes']

for route in routes:
    collection.insert_one(route)
    

pprint.pprint(collection.find())
