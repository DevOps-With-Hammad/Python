# Who will pay the Bill
import random

str_input = input("pass me all the names\n ")
Ox = str_input.split(", ")
num_list = len(Ox)
randch = random.randint(0, num_list-1)
personwhopays = Ox[randch]
print(personwhopays + " he is going to pay today ")