
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
    "/": divide
}

num1 = int(input("What's your first number?: "))
num2 = int(input("What's your second number?: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick and operation from the line above: ")

calculation_function = operations[operation_symbol]
answer = calculation_function(num2, num1)

print(f"{num1} {operation_symbol} {num2} = {answer}")


