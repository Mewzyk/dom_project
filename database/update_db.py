import json
import pprint
import requests
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

API_KEY = '200212432-f3aa9be57f04ce46760dce00bef02b2d'
API_URL = 'https://www.mountainproject.com/data/get-routes-for-lat-lon?lat=%d&lon=%d&maxDistance=200&key=%s' % API_KEY

client = MongoClient()
collection = client.getRoutey.routes


r = requests.get('https://www.mountainproject.com/data/get-routes-for-lat-lon?lat=36.5&lon=-121.202&maxDistance=10&minDiff=5.6&maxDiff=5.8&key=200212432-f3aa9be57f04ce46760dce00bef02b2d')
database = r.json()
routes = database['routes']

for route in routes:
    try:
        collection.insert_one(route)
    except DuplicateKeyError:
        pass

pprint.pprint(collection.find())
