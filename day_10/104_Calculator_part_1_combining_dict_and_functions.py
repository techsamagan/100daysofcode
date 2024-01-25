def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": multiply
}
while True:
    num1 = int(input("What's the first number?: "))
    print("'+', '-', '*', '/'")
    oper = input("Enter operations: ")
    num2 = int(input("What's the second number?: "))
    calculation_function = operations[oper]
    print(calculation_function(num1, num2))

