#Opens a URL, parses XML data, and finds all the trees that contain the phrase "Count".  Sums & counts these phrases.
import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location:')
count = 0
sum = 0

print('Retrieving:', url)
xml = urllib.request.urlopen(url).read()
print('Retrieved:', len(xml), 'characters')

tree = ET.fromstring(xml)
results = tree.findall('.//count')
for i in results:
    sum = sum + int(i.text)
    count = count + 1
print('Count', count)
print('Sum:', sum)
