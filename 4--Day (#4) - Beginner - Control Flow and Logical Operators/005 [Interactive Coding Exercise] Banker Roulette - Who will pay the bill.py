# Who is Gonna Pay the full bill for our food
# Do you know how to use the Split Function??

Str_inp = "Ahmed,Ali,Mustafa,Emarra"
op = Str_inp.split(",")
print(op)
# Good.
# output should be like that
# ['Ahmed', 'Ali', 'Mustafa', 'Emarra']

# Now How about getting the names from the user using the input function.
# >>
name_Str = input("Pls Every Body's name Separated by comma . ")
names = name_Str.split(",")
print(names)

# This is wonderful result to have here you really did magic today :).

# Do we need the len() function ?? I don't know you tell me .
# We also gonnaa need to Import the  RANDOM model
import random
Names_Str = input("Names Pls separated by comma. \n ")
Names = Names_Str.split(",")
print(len(Names))
Num_of_items = len(Names)
chois = random.randint(0, Num_of_items-1)
Chois = Names[chois]
print("Person who is gonna pay for our meal today is \n" + Chois)

