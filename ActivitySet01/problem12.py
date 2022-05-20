# Regular Expressions
# https://www.py4e.com/lessons/regex
# The basic outline of this problem is to read the file, 
# look for integers using the re.findall(), looking for a 
# regular expression of '[0-9]+' and then converting the 
# extracted strings to integers
#  and summing up the integers.
import re
lst=[]
file=open("py4e_regex.txt")
for line in file:
    words=re.findall('[0-9]+',line)
    lst.append(words)
a=[]
for x in lst:
    if x!=[]:
        for y in x:
            a.append(y)
sum=0
for i in a:
    sum=sum+int(i)
print(sum)


