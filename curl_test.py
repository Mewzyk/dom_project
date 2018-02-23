import requests
import json

r = requests.get('https://www.mountainproject.com/data/get-routes-for-lat-lon?lat=36.5&lon=-121.202&maxDistance=10&minDiff=5.6&maxDiff=5.8&key=200212432-f3aa9be57f04ce46760dce00bef02b2d')

db = r.json()
climbingRoutes = db['routes']

print('Printing Example Data set')
print('-------------------------')

for route in climbingRoutes:
	print('==========================')
	for key in route.keys():
		print(key, '-->', route[key])
