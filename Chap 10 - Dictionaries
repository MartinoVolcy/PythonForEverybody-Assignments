#The dictionary data structures allows us to store multiple values in an object and look up the values by their key.

#9.4

#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
file1 = open(name)
storage = dict()
for line in file1:
    if line.startswith('From '):
        words = line.split()
        name = words[1]
        storage[name] = storage.get(name,0) + 1   
    else:
        continue
largest = 0
largestName = None
for key in storage:
    if storage[key] > largest:
        largest = storage[key]
        largestName = key
print(largestName, largest)
