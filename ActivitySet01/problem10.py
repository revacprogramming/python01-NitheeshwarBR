#dictionaries
# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's 
# mail address to a count of the number of times they appear in the file. After the dictionary is produced, 
# the program reads through the dictionary using a maximum 
# loop to find the most prolific committer.
lst=[]
mails={}
file=open(input())
for i in file:
    if i.startswith('From:'):
        continue
    elif i.startswith('From'):
        words=i.split()
        word=lst.append(words[1])
for i in lst:
    if i not in mails:
        mails[i]=1
    else:
        mails[i]=mails[i]+1
max=0   
for i in mails:
    if mails[i]>max:
        max=mails[i]
        largest=i
    elif mails[i]<max:
        continue
        
print(largest,mails[largest])