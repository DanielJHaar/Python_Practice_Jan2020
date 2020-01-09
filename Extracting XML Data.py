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
