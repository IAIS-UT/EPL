import mysql.connector
import os
import glob



list_of_files = glob.glob(r'C:\Users\Hamed\Desktop\ALL_FILES\*.properties')
for i in range(len(list_of_files)):
    open(list_of_files[i], 'w').close()


#here we connect to database and run query
f = []
db = mysql.connector.connect(host="127.0.0.1",       # your host, usually localhost
                             user="root",               # your username
                             passwd="mysql123sjb",      # your password
                             db="Ho3Test",
                             port="8888")              # name of the data base

cur = db.cursor()

q = "SELECT * FROM configs WHERE code=22222 and project = 'EPL'"
cur.execute(q)


for row in cur.fetchall():                              #reading query output line by line
     f.append(row[0:])

#now we write contents of list"f" into "sample.txt
open('sample.txt', "w").close()

with open('sample.txt', 'a') as sample:
    for item in f:
        w = list(item)
        for i in range(len(w)):
            if i == 7:
                sample.write(str(w[i]) + '\n')
            else:
                sample.write(str(w[i]) + ",")


#then we read through "sample.txt" line by line to write contents of each file inside it
addr = []
my_file = open("sample.txt", "r")
for line in my_file:
    if line != '\n':
        l = list(line.split(','))
        l = [x.strip(' ') for x in l]
        addr.append(l[2])

for i in range(len(addr)):
    open(addr[i], 'w').close()

my_file = open("sample.txt", "r")
for line in my_file:
    if line != '\n':
        l = list(line.split(','))
        l = [x.strip(' ') for x in l]
        contents = l[4] + "=" + l[5]
        filename = r"C:\Users\Hamed\Desktop\ALL_FILES" + r'\\' + l[2]
        with open(filename, 'a') as filename:
            filename.write(contents+'\n')
            filename.close()


print("successful!")

