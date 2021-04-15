# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.



name = input("Enter file:")

li=list()

with open(name,"r") as textfile:
    for i in textfile:
        if i.startswith("From "):
            asd = i.split()
            li.append(asd[1])
            
di = dict()

for a in li:
    di[a] = di.get(a,0) + 1 
    
key = 0
value = 0

for k,v in di.items():
    if v > value:
        value = v
        key = k
print(key,value)