# Nested if >>>>>>> if inside if.

# First do the first if statement.

# Make a Var to hold the review.
Var_cc = int(input("your value pls :- \n "))

# The If statement
if Var_cc >= 120:
    print("you can drive boy you made it \n \n here is a second Check pls answer correctly")
    Age = int(input("what is your age dear :- \n "))
    if Age >= 18:
        print("congratulation sir \n you are ready to drive ")
    elif Age >= 17:
        print("you ready to take tests and a lessons in driving  ")
    elif Age >= 15:
        print("you're gonna take just lessons \n feel free to ask dont give up trying ")
    elif Age >= 12:
        print("you're too young for that dear \n you should get company with your parents ")
    elif Age >= 9:
        print(" you are a baby. you know that ! \n what your gonna do set on me ")

else:
    print("Iam sorry to tell \n you sir can't drive")
# end of the Programme.
