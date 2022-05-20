# input? 1 2
# 1+2 is 3
def add(a,b):
    sum=a+b
    return sum


def output(a,b,sum):
   print(a+b is sum)

def main():
    a,b=input("input? ").split()
    sum = add(a,b)
    output(a,b,sum)
name='main'
if name == 'main':
    main()
