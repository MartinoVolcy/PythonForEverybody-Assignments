#The tuple is a Python data structure that is like a simple and efficient list.

#10.2

#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
file1 = open(name)
dct = dict()
for line in file1:
    if line.startswith("From "): 
        lst = line.split()
        num = lst[5]
        time = num.split(":")
        dct[time[0]] = dct.get(time[0],0) + 1
ftime = sorted(dct.items())
for (k,v) in ftime:
    print(k,v)
