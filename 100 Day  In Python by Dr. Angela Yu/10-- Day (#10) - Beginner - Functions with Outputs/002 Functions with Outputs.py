# 002 Functions with Outputs
def cal():
    result =3*3
    return result


# another way.

def cal1():
    resltt = 5*5
    return resltt


# Format name with function.
def format_name(f_name, l_name):
    # convert the name to title name no matter what is the inserting.
    print(f_name.title())
    print(l_name.title())
# Displying the output with the defined function
format_name("hAMmad", "iBrahim\n ")

# Output should be like that
# Hammad
# Ibrahim


# Format name with function.
def format_name1(ff_name, ll_name):
    # convert the name to title name no matter what is the inserting.
    format_ff_name1 = ff_name.title()
    format_ll_name1 = ll_name.title()

    print(f"Your output should be like . \n\n{format_ff_name1} {format_ll_name1}")
# Displying the output with the defined function
format_name1("hAMmad", "iBrahim")

# Output should be like that
# Hammad Ibrahim


# Way ##3003 :-
# Format Name 3

def Format_name2(F_Name, L_name):
    # declaring the title for the parameters
    Formated_F_name = F_Name.title()
    Formated_L_name = L_name.title()
    # Return the function
    return f"{Formated_F_name} {Formated_L_name}"
# Printing the output here ---
print(format_name("\nThe output should be like \nhaMMAD", "ibRAHIM"))



"""
    That is for today with the # Return Function
    If you need anything els just follow the guide. 
    Wish me luck 
"""







