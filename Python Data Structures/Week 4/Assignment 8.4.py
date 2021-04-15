# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not 
# append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt


fname = input("Enter file name: ")

li = list()

with open(fname,"r") as textfile:
    for i in textfile:
        words = i.rstrip().split()
        
        for a in words:
            if a in li:
                continue
            else:
                li.append(a)
                
li1 = sorted(li)

print(li1)



# It can be solved in this way too


fname = input("Enter file name: ")

li=list()

with open(fname,"r") as textfile:
    for i in textfile:
        words = i.rstrip().split()
        li = li + words
        
final_list = set(li)
final_list = sorted(final_list)  # returns a list of the elements in sorted order

print(final_list)
