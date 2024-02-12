import operator

def calculator():
    """Implements a calculator using a dictionary lookup with error handling and support for basic operations (+, -, *, /).

    Returns:
        None
    """

    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv  # Use true division for floating-point results
    }

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            op = input("Enter an operation (+, -, *, /): ")
            if op not in operators:
                raise ValueError("Invalid operation symbol.")
            num2 = float(input("Enter the second number: "))
            calculation = operators[op](num1, num2)
            print(f"{num1} {op} {num2} = {calculation}")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            if input("Do you want to continue (y/n)? ").lower() != 'y':
                break

if __name__ == '__main__':
    calculator()
