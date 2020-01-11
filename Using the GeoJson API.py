#Calling a JSON API
#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for
#a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON.
#A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

import urllib.request, urllib.parse, urllib.error
import json

#Test Value and Desired Variable
serviceurl = 'http://py4e-data.dr-chuck.net/json?'
address = input('Enter location: ')

#Connecting to url
url = serviceurl + urllib.parse.urlencode({'address': address, 'key': 42})
print('Retrieving', url)

#Requesting data from URL and reading data
data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characers')

#Loading data from UTF-8 into JSON format and identifying the piece to be selected
jsdata = json.loads(data)
place_id = jsdata["results"][0]["place_id"]
print('Place ID: ',place_id)
