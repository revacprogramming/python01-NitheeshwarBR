#tuple:
# Write a progam to read through mbox-short.txt anf figure out the distribution by hour of the day
# for each of the messages. you can pull the hour out from the from line by finding and the time and the splitting the string second time using a COLON
# From stephen.marquard@uct.ac.za Sat jan 5 09:14:16 2008
#  once you have accumulated the counts for each hour ,print out the counts
file=open('mbox-short.txt')
lst=[]
for line in file:
    if line.startswith('From:'):
        continue
    elif line.startswith('From'):
        words=line.split()
        word=words[5]
        lst.append(word)
hour=[]
for i in lst:
    words=i.split(':')
    word=words[0]
    hour.append(word)
    hour.sort()
hours={}
for hrs in hour:
    if hrs not in hours:
        hours[hrs]=1
    else:
        hours[hrs]+=1
res=hours.items()
for hr,c in res:
    print(hr,c)
  



