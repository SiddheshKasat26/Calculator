from art import logo

import os 

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Create a Dictionary
Operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def clear_console():
    os.system('cls')

def calculator():

    print (logo)

    run = False

    num1 = float(input("What's the first number?: "))
    for symbol in Operations:
        print (symbol)

    while not run:
        Operation_symbol = input("Pick an operation: ")

        num2 = float(input("What's the next number?: "))

        calculation_function = Operations[Operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {Operation_symbol} {num2} = {answer}")

        should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. " )

        if should_continue == 'y':
            num1 = answer

        elif should_continue == 'n':
            run = True
            clear_console()
            calculator()

calculator()