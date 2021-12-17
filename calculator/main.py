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

num1 = int(input("What's the first number: "))
for key in operations:
    print(key)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number: "))

calculation_func = operations[operation_symbol]
answer = calculation_func(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")


while True:
    cont = input(
        f"type 'y' to continue calculating with the {answer} or type 'n' to exit.: ")
    if cont == 'n':
        print("Thank you for using calculator")
        break

    operation_symbol = input("Pick another operation: ")
    num3 = int(input("What's the next number: "))

    calculation_func = operations[operation_symbol]
    second_answer = calculation_func(answer, num3)

    print(f"{answer} {operation_symbol} {num3} = {second_answer}")

    answer = second_answer
