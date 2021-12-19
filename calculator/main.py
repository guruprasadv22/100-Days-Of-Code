# Calculator


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


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = int(input("What's the first number: "))
    for key in operations:
        print(key)
    # operation_symbol = input("Pick an operation from the line above: ")
    # num2 = int(input("What's the second number: "))

    # calculation_func = operations[operation_symbol]
    # answer = calculation_func(num1, num2)

    # print(f"{num1} {operation_symbol} {num2} = {answer}")
    should_continue = True

    while should_continue:

        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number: "))

        calculation_func = operations[operation_symbol]
        answer = calculation_func(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        cont = input(
            f"Type 'y' to continue calculating with the {answer} or type 'end' to exit or 'new' to start a new calculation: ")

        if cont == 'new':
            should_continue = False
            calculator()
        if cont == "end":
            break

        num1 = answer


calculator()
