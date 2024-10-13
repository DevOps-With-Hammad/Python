# # Problem 1
# """
# Use Python to calculate how many different passwords can be formed with 6 lower case English letters
#  (excludes any character not found in the English alphabet).
# For a 1 letter password, there would be 26 possibilities.
# For a 2 letter password, each letter is independent of the other, so there would be 26 times 26 possibilities.
# Using this information, print the amount of possible passwords that can be formed with 6 letters.
# """


# Answer :-
"""
To calculate the number of possible 6-letters passwords we use the fact that each letter in the password
 can be chosen independently form 26 lowercase English letters.

FOR each position int the password :
- There are 26 possible choices for the first letter.
- There are 26 possible choices for the second letter.
- This pattern will continue for all the 6 letters.

The total number of different password is 26* 26* 26* 26* 26*26 = 26 **6
Calculating this, we get 308,915,776 possible passwords

"""
# let's give it a try ..

english_letters = 26
Password_letters = 6
print(f" The  value of {str(english_letters ** Password_letters)} is the possible passwords  ")