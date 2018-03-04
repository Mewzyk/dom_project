#!/usr/bin/python3
import time
import json
import pprint
import requests
import logging
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

API_URL = 'https://www.mountainproject.com/data/get-routes-for-lat-lon?lat=%f&lon=%f&maxDistance=200&key=200212432-f3aa9be57f04ce46760dce00bef02b2d'

logging.basicConfig(filename='update_db.log', level=logging.DEBUG)
client = MongoClient()
collection = client.getRoutey.routes

def get_routes(latlon):
    request_url = API_URL % (latlon['lat'], latlon['lon'])
    logging.debug(request_url)
    r = requests.get(request_url)
    database = r.json()
    return database['routes']

def add_routes(routes):
    for route in routes:
        try:
            collection.insert_one(route)
        except DuplicateKeyError:
            pass

def main():
    routes = []
    for latlon in client.getRoutey.locations.find():
        routes += get_routes(latlon)
    add_routes(routes)

if __name__ == '__main__':
    while True:
        main()
        time.sleep(604800)
