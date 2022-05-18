# input? 1 2
# 1+2 is 3
def add(a, b):
    sum=a+b
    return sum


def output(a, b, sum):
    pass  # ...


def main():
    a, b = input_two_numbers()
    sum = add(a, b)

    output(a, b, sum)


if __name__ == '__main__':
    main()
