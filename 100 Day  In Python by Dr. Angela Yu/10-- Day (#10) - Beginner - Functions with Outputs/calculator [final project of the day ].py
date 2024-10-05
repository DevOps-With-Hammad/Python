# 006 Calculator Part 1 Combining Dictionaries and Functions.
"""First:- defining the operation function in the code as we go.
 Add
 """


def add(n1, n2):
    return n1 + n1


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

num1 = int(input("First Number Plz : "))
num2 = int(input("Second Number Plz : "))
for symbol in operation:
    print(symbol)
operation_sympols = input("Plz Pick an operation from the line above :")
calculation_function = operation[operation_sympols]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_sympols} {num2} = {answer}")

# wish Me luck On this first Part.