# Multiple If condition in one Tasks.

Height = float(input("pls Enter your Height inn CMs :- \n "))
if Height >= 120:
    print("you can drive")
    Age = int(input("Pls enter your age to determine the price\n "))
    if Age < 12:
        print("you're gonna cost 5$ ")
    elif Age >= 12 & Age < 18:
        print("you're gonna cost 7$ ")
    elif Age >= 18:
        print("you're gonna cost 10$  ")
    Wanted_Photos = input("Pls confirm with photo or not type Y or N \n")
    if Wanted_Photos == "Y":
        print("here is your bill +3$ for the Photo")
    else:
        print("okay here is your bill ")
else:
    print("you can't drive, \n we're sorry to inform you that, pls try aging. \n on the height 120 CMs")
