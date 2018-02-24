import requests
import json

r = requests.get('https://www.mountainproject.com/data/get-routes-for-lat-lon?lat=36.5&lon=-121.202&maxDistance=10&minDiff=5.6&maxDiff=5.8&key=200212432-f3aa9be57f04ce46760dce00bef02b2d')

database = r.json()
climbingRoutes = database['routes']

print('Printing Example Data set')
print('-------------------------')


#Loop that prints everything out
#Climbing routes contains a List of routes
#Each route is a dictionary with a list of keys
#This function prints out
#========================
# KEY --> route[KEY]
for route in climbingRoutes:
	print('==========================')
	for key in route.keys():
		print(key, '-->', route[key]
print('hello world')


