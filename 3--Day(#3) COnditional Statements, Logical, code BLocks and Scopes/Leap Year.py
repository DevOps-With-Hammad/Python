# Leap Year Example
Year = int(input("Please enter your Year \n here to check it if it is \n  a leap Year or not "))
# Define the equation
if Year % 4 == 0 & Year % 100 == 0 & Year % 400 == 0:
    print("It is a Leap Year ")
else:
    print("not a leap year ")
