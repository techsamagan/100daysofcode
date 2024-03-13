def add(*args):
    print(args)
    sum=0
    for i in args:
        sum += i
    print(sum)
    return sum

add(3,4,56,6)