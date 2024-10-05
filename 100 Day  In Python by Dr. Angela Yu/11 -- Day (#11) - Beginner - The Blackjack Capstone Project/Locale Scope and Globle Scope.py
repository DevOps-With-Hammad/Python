################################## Scope Variables ###############################
enemies = 1


def increase_enemies():
    enemies = 2
    print(f'enemies inside the function : {enemies}')


increase_enemies()
print(f'enemies outside the function : {enemies}')


# """
# Local VS Global Variables .
# """
###################### Local Scope Vs Global Scope ############
def drink_potion():
    potion_strenght = 2
    print(f'your potion value is :{potion_strenght}')


drink_potion()

#######################Here is another function to Inside function ############
phone_number = 99


def phone_store():
    def phone():
        phone_x = 22
        print(f'Here is your phone out function {phone_number}')


print(f'Your phone number with global scope : {phone_number}')



