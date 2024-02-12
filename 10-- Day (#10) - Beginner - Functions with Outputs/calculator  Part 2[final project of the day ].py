# Calculator Part 2

# 006 Calculator Part 1 Combining Dictionaries and Functions.
"""First:- defining the operation function in the code as we go.
 Add
 """


def add(n1, n2):
    return n1 + n2


"""Second:-
 subtraction 
"""


def subtract(n1, n2):
    return n1 - n2


"""Third :- 
Multiply
"""


def multiply(n1, n2):
    return n1 * n2


"""Forth :-
Division
"""


def divide(n1, n2):
    return n1 / n2


""" Operation part 
Adding symbols
"""

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    num1 = float(input("First Number Plz : "))
    for symbol in operation:
        print(symbol)
    should_continue = True #

    while should_continue:
        operation_symbols = input("Plz Pick an operation : ")
        num2 = float(input("Next Number Plz : "))
        calculation_function = operation[operation_symbols]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbols} {num2} = {answer}")

        if input((f"Type 'y' to continue calculating with {answer},"
                  f" or type 'n' to start a new calculation ")) == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()

# This code Has many bugs :)
