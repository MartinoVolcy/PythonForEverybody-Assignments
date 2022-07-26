#Web services allow a program to access data available in a different server.
#---------------------------------------------------------------------------------------------------------------------------------------------
#Extracting Data from XML

#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
#The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, 
#compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1443650.xml'
data = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(data)
nums = tree.findall('.//count')
count = 0
for i in nums:
  count += int(i.text)
print(count)

#----------------------------------------------------------------------------------------------------------------------------------------------

#Extracting Data from JSON

#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. 
#The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, 
#compute the sum of the numbers in the file and enter the sum below:

import json
import urllib.error, urllib.request, urllib.parse
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1443651.json'
data = urllib.request.urlopen(url, context=ctx).read()  
jsonData = json.loads(data)

count = 0
x = sum([count + i['count'] for i in jsonData['comments']])
print(x) 

#---------------------------------------------------------------------------------------------------------------------------------------------------

#Calling a JSON API

#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. 
#The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, 
#and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

import json
import urllib.error, urllib.request, urllib.parse
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = 'Farmingdale State University'

apiKey = '42'
api = 'http://py4e-data.dr-chuck.net/json?'
fUrl = api + urllib.parse.urlencode({'address': address, 'key': apiKey})
data = urllib.request.urlopen(fUrl, context=ctx).read()  
jsonData = json.loads(data.decode())

id = jsonData['results'][0]['place_id']
print(id)
