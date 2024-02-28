def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def calculator(operation, x, y):
    """A higher-order function that takes an operation function and two operands."""
    return operation(x, y)

# Example usage
x, y = 10, 5
print("Add:", calculator(add, x, y))
print("Subtract:", calculator(subtract, x, y))
print("Multiply:", calculator(multiply, x, y))
print("Divide:", calculator(divide, x, y))
