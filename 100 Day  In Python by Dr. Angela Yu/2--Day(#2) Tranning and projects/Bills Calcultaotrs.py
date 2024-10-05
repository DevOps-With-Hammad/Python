# Welcome to the tip Calculator
# len() function.
print(len("hello!"))
# data Types.
# Subscript- printing out a specific character from the code * as you can see

print("helo! " [0])
print("helo! " [2])
print("helo! " [5])

# Integer.
print(123 + 123 + 546 + 236)
# float
print(3.14 + 5.20)
# boolean
print("ture")
print("false")


# what if you need to take a username and to print it out with a message
# saying the number of characters of that username.

# If you write it that way, you gonna git error in the second stage which is the len() function.
# print("your name is =" + len(input("what is your name dear ??")))

print("your name is =" + str(len(input("what is your name dear ??"))))

# SO how to fix it??
# give it a Var value as you can see.
Num_char = len(input("what is your name dear ??"))
New_num_char = str(Num_char)
print("Hello Dear, Your name has " + New_num_char + " Characters ")
# print("Hello Dear, Your name has " + Num_char + " Characters ")
# TypeError: can only concatenate str (not "int") to str
print((type(Num_char)))  # to know data type to avoid the error
# End of today Lesson HAHAHA..

