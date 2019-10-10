import mysql.connector
import os
import glob
from shutil import copyfile

print("processing...")
x = os.path.abspath("")
o1 = os.path.abspath("FILES")
o2 = o1 + "/*.properties"


#connecting to database and running query
f = []

db = mysql.connector.connect(host='127.0.0.1',  # your host, usually localhost
                             user='root',  # your username
                             password='',  # your password
                             database='Ho3Test',
                             port=8888)  # name of the data base


cur = db.cursor()

q = "SELECT * FROM configs WHERE code=22222 and project = 'EPL'"
cur.execute(q)

for row in cur.fetchall():  # reading query output line by line
    f.append(row[0:])

# now we write contents of list"f" into "config.txt
open('config.txt', "w").close()

with open('config.txt', 'a') as config:
    for item in f:
        w = list(item)
        for i in range(len(w)):
            if i == 7:
                config.write(str(w[i]) + '\n')
            else:
                config.write(str(w[i]) + ",")
config.close()

# then we read through "config.txt" line by line to write contents of each file inside it
addr = []
my_file = open("config.txt", "r")
for line in my_file:
    if line != '\n':
        l = list(line.split(','))
        l = [x.strip(' ') for x in l]
        addr.append(l[2])
		
for i in range(len(addr)):
    open(addr[i], 'w').close()



#connecting to db once more to retrieve the addresses of file and copy them in those addresses 
h = []
db = mysql.connector.connect(host='127.0.0.1',  # your host, usually localhost
                             user='root',  # your username
                             password='',  # your password
                             database='Ho3Test',
                             port=8888)  # name of the data base

cur = db.cursor()


#we only need the 'name' and 'path' of a file 
qq = "SELECT filename,path FROM fileconfig WHERE project = 'EPL'"
cur.execute(qq)

for row in cur.fetchall():  # reading query output line by line
    h.append(row[0:])

open('fileconfig.txt', "w").close()


#writing filename and path to 'fileconfig.txt'
with open('fileconfig.txt', 'a') as fileconfig:
    for item in h:
        p = list(item)
        for i in range(len(p)):
            if i == 3:
                fileconfig.write(str(p[i]) + '\n')
            else:
                fileconfig.write(str(p[i]) + ",")
fileconfig.close()



#putting contents of 'fileconfig.txt' into 'myconf' list
with open('fileconfig.txt', 'r') as f:
    myconf = [line.strip() for line in f]   

myconf = [myconf[0].split(",") for i in myconf]
#here we make 2 lists and put filenames in one and addresses in the other one
myconf_filename=[]
myconf_addr=[]
for i in range (len(myconf[0])):
    if i%2 == 0 :
        myconf_filename.append(myconf[0][i])
    if i%2 == 1 :
        myconf_addr.append(myconf[0][i])


t=list(set(myconf_addr))

for i in range(len(t)):
    o2 = t[i] + "/*.propertiies"
    list_of_files = glob.glob(o2)
    for i in range(len(list_of_files)):
        open(list_of_files[i], 'w').close()

#clearing all files in their address so that we dint write contents twice or more

my_file = open("config.txt", "r")
for line in my_file:
    if line != '\n':
        l = list(line.split(','))
        l = [x.strip(' ') for x in l]
        for i in range (len(myconf_filename)):
            if myconf_filename[i] == l[2]:
                indx = myconf_filename.index(myconf_filename[i])
                break
        indx = int(indx)
        newaddr = myconf_addr[indx]
        filename ="." +  newaddr + "/" + l[2]
        open(filename, "w").close()
        
        

#writing contents into each file , then getting its address from 'myconf_addr' and putting it there

my_file = open("config.txt", "r")
for line in my_file:
    if line != '\n':
        l = list(line.split(','))
        l = [x.strip(' ') for x in l]
        contents = l[4] + "=" + l[5]
        if len(l)>8:
            for i in range( 6 ,len(l)-2):
                contents = contents + "," + l[i]
        #contents = l[4] + "=" + l[5]
        for i in range (len(myconf_filename)):
            if myconf_filename[i] == l[2]:
                indx = myconf_filename.index(myconf_filename[i])
                break
        indx = int(indx)
        newaddr = myconf_addr[indx]
        filename ="." +  newaddr + "/" + l[2]
        with open (filename, "a") as ff :
            ff.write(contents + '\n')
            ff.close()



o3 = os.path.abspath("")


#here we remove the .properties files with 0 Kb size
o3 = o3 + "/*.properties"
list_of_files2 = glob.glob(o3)
for i in range(len(list_of_files2)):
    f = open(list_of_files2[i], 'r')
    if os.stat(list_of_files2[i]).st_size == 0:
        f.close()
        os.remove(list_of_files2[i])


print("successful!")


