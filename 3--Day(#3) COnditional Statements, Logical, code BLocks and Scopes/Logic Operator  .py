# Logical operator.

print("Welcome Sir to The driver Licence Reg")
# Take the output from the user.
Height = int(input("Pls Sir Enter your Height Here \n "))
if Height >= 120:
    print("Good News you can Ride ")
    Age = int(input("Pls sir Enter your Age :- \n "))
    if Age < 12 :
        print(" You're charge is 5$ per Ticket ")
    elif Age > 12 & Age <= 18:
        print("you're gonna charge  7$")
    elif Age > 18:
        print("you're gonna charge 12$ ")
    else:
        print("you're gonna charge 0$")
    photo = input("with photo or not pls type Y or N \n ")
    if photo == "Y":
        print(" your charge is ")
    else:
        print("nothing to put here")
else:
    print("Sorry Sir you not allowed to have a licence because your height is under 120 CMs")
