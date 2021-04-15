# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output 
# as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.


fname = input("Enter file name: ")

li = list()

with open(fname,"r") as asd:
    for i in asd:
        if i.startswith("X-DSPAM-Confidence:"):
            asd = i.split()
            li.append(asd[1])
            
count = 0
total = 0

for a in li:
    count = count + 1
    total = total + float(a)   # In the list all the numbers will be strings. So I have to convert it into float
    
average = total/count

print("Average spam confidence:",average)

