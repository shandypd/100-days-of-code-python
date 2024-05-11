from art import logo
import os


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

while True:
    print(logo)

    num1 = float(input("What's the first number?: "))

    for sign in operations:
        print(sign)

    should_continue = "y"
    while should_continue == "y":
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        answer = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")

        should_continue = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
        )

        num1 = answer

    os.system("clear")
