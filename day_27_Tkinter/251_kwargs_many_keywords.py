def add(*args):
    print(args)
    sum=0
    for i in args:
        sum += i
    print(sum)
    return sum

add(3,4,56,6)

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    
calculate(2, add=3, multiply = 5)