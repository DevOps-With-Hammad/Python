# Example: Variable Casting in Python
# In Python, we can change the data type of a variable using casting functions like int(), float(), bool(), etc.

# Initial variable 'name' as a string
name = " Python Developer "
print(name)  # Output: Python Developer

# Casting Example with int, float, and boolean
# We are converting a string to an integer using the int() function
age = int("15")
print(age)  # Output: 15

# When we check the type of the 'age' variable, it will show <class 'int'>
# This is because even though we initially provided the number as a string, the int() function converts it into an integer.
print(type(age))  # Output: <class 'int'>

# Proof of integer type: We can perform arithmetic operations on the 'age' variable
print(age * 2)  # Output: 30

# Let's define another variable 'age1', but this time it remains a string
age1 = "15"
print(type(age1))  # Output: <class 'str'>

# Since 'age1' is treated as a string, it cannot be used in mathematical operations.
# If we multiply a string, it will repeat the string.
print(age1 * 3)  # Output: 151515
