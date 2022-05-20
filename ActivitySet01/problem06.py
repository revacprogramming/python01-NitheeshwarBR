# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
#  Once 'done' is entered, print out the largest and smallest of the numbers. 
#  If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message 
#  and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below.
max=0
min=0
while True:
    try:
        a=input("Enter number\n")
        if a=='done':
            break
        num=int(a)
        if max==0 or num>max:
            max=num
        if min==0 or num<min:
            min=num
    except:
        print('invalid input\n')
print('largest=',max)
print('smallest=',min)

    