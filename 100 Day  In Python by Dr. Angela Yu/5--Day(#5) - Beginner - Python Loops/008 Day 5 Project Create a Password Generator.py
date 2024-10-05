# Welcom to the pypassword generator.
# Password generator.

# import the random Function.
import random
Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
Sympols = ['+', '/', '*', '!', '@', '#', '$', '%', '^', '&', '-']
print("Welcome to the PypasswordGenerator!\n \n ")

nr_letters = int(input(f"How many letters?? \n"))
nr_sympols = int(input(f"How Many sympols\n"))
nr_numbers = int(input(f"how many numbers \n"))
# Here is the magica of our programe .
# EasyPAssword
# for char in range(1, nr_letters + 1):
# for char in range(1, nr_numbers + 1):
# password += str(random.choice(numbers))
# for char in range(1, nr_sympols + 1):
# password += random.choice(Sympols)

# print(f"Here Is your Password :\n{password}")

# Hard Way
password_list = []

for char in range(1, nr_sympols + 1):
    password_list += random.choice(Sympols)
for char in range(1, nr_numbers + 1):
    password_list += str(random.choice(numbers))
for char in range(1, nr_letters + 1):
    password_list += random.choice(Letters)
print(password_list)
random.shuffle(password_list)
print(password_list)
password = ""
for char in password_list:
    password += char
    print(f"Here is your password : \n {password}")
