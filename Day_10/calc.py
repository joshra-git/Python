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
    "/": divide,
}

num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
operational_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))
calculation_function = operations[operational_symbol]
first_answer = calculation_function(num1, num2)
print(f"{num1} {operational_symbol} {num2} = {first_answer}")

continue_calcs = True
while continue_calcs:
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation: ")
    num3 = int(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    second_answer = calculation_function(first_answer, num3)
    print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
    first_answer = second_answer
    more = input(f"Do you wish to continue with {first_answer}? Type 'y' for yes and 'n' for no.")
    if more == "n":
        continue_calcs = False