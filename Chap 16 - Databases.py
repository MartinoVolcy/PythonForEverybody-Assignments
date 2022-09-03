#Counting Emails
#This application will read the mailbox data (mbox.txt) 
#and count the number of email messages per organization (i.e. domain name of the email address) using a database 
#with the following schema to maintain the counts.

import sqlite3

file = open('mbox.txt')

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

dct = {}

for line in file:
    if line.startswith('From: '):
        idx = line.find('@')
        org = line.split()[1].split(line[idx],1)[1] 
        dct[org] = dct.get(org, 0) + 1
        print(org)

for v,k in dct.items():
    cur.execute('''
INSERT INTO Counts (org, count) VALUES (?,?)''', (v,k))
   
print(dct)
        
conn.commit()
cur.close()

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

