# 003 Multiple return values.

# Function with output.

def FormatName(Fname, LName):
    # Title Name
    # if you want to terminate function early
    if Fname == "" and LName =="":
        return "You Did not provide any information here pls try again "
    # here
    fname = Fname.title()
    lname = LName.title()
    return f"{fname} {lname}"


print(FormatName(input("YOur first name is : \n "),
                 input("Your Last Name is : \n ")))
