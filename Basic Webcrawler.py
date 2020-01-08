#Basic webcrawler that retrieves all the anchor tags from a web page
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#Python requests to connect to webpage, and BeautifulSoup cleans up HTML code for more accurate parsing
url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
