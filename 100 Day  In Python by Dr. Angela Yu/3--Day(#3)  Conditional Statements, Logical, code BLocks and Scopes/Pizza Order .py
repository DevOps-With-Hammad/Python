# Pizza programme Order in Python
Pizza_size = input("Welcome to Python Pizza  home Sir, \n  Medium, small or large, Sir! \n pls press  S, M or L ")
Pizza_with_pepperoni = input("Do you want Pepperoni ? Pls press Y or N \n ")
Pizza_with_extra_chess = input("Do you want Extra chess?  pls Type Y or N \n")
# Here is the magic of if statement to deliver Pizza
# write your code here >>>>>
bill = 0
if Pizza_size == "S" & Pizza_with_pepperoni == "Y" & Pizza_with_extra_chess == "Y":
    bill += 15 + 2 + 2
    print(f"Here is your pizza sir, your bill is {bill}")
elif Pizza_size == "M" & Pizza_with_pepperoni == "Y" & Pizza_with_extra_chess == "Y":

    print(f"Here is your Pizza\n your bill is  ")
elif Pizza_size == "L" & Pizza_with_pepperoni =="Y" & Pizza_with_extra_chess == "Y":

    print(f"Here is your Pizza Sir \n Your Bill is ")
else:
    print("Pls Try again with another order ")

