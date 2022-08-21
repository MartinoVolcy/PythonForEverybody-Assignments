#We take a quick look at how data moves across the network using the HyperText Transport Protocol (HTTP) and how we write programs to read data across the network.

#Request-Responce Cycle
#Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.
#------------------------------------------------------------------------------------------------------------------------
#Scraping Numbers from HTML using BeautifulSoup
#In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. 
#The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1443648.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

lst = list()
tags = soup('span')
for tag in tags:
  lst.append(int(tag.contents[0]))
print(sum(lst))
#-----------------------------------------------------------------------------------------------------------------------------

#Following Links
#In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
#The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, 
#scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
position = int(input("Enter Link Position: "))
count = int(input("Enter the count: "))

def nxtURL(url, position):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tag = tags[position - 1]
    return tag.get('href', None)

fTag = nxtURL(url, position)
while count - 1 > 0:
  fTag = nxtURL(fTag, position)
  count = count - 1

print(re.findall('_([A-Z][a-z]+)', fTag))
