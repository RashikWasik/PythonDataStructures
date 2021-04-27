# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.



name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

li = list()

with open(name,"r") as textfile:
    for i in textfile:
        if i.startswith("From "):
            asd = i.split()
            jkl = asd[5].split(":")
            li.append(jkl[0])
            li = sorted(li)
            
di = dict()

for a in li:
    di[a] = di.get(a,0) + 1
    
for k,v in di.items():
    print(k,v)


    
    
    
    
    

    
    
# To sort the dictionary instead of the list

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

li = list()

with open(name,"r") as textfile:
    for i in textfile:
        if i.startswith("From "):
            asd = i.split()
            jkl = asd[5].split(":")
            li.append(jkl[0])
            
di = dict()

for a in li:
    di[a] = di.get(a,0) + 1
    
di = sorted([(k,v) for k,v in di.items()])  # It returns a list 
    
for k,v in di:
    print(k,v)

