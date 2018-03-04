from flask import Flask
from flask import render_template
import requests
import json

print("file test")
with open('routeInfo.json', 'w') as outfile:
    json.dump("hi", outfile)

