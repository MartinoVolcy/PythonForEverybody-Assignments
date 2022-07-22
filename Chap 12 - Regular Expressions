#Regular Expressions allow us to search for patterns in strings and extract data from strings using the regular expression programming language.

#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

#I did this with Network programming(Next Chapter) because my computer wouldn't download the file for some reason

import re
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/regex_sum_1443646.txt') 

lst = list()
for line in fhand:
    nums = re.findall('[0-9]+', line.decode())
    for i in nums:
        lst.append(int(i))
print(sum(lst))
