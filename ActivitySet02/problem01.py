# Enter 1st Number? 1
# Enter 2nd Number? 2
# Sum of 1 and 2 is 3

def add(a,b):
    sum=a+b
    return sum
def main():
    a = int(input('Enter 1st Number? '))
    b = int(input('Enter 2nd Number? '))

    c = add(a,b)
    print('Sum of',a,'and',b,'is',c)
main()
