# 16. [GA] Level 9 Final Exercise Simple Bank Account Manager (17- answer )
# Instruction : -
"""
- Create a class called Bank Account with attributes for account number and balance
- Add methods to the $ Bank account class for deposit , withdrawal, and balance check.
- Create a dictionary called accounts to store multiple Bank account objects
- Implement a user interface to interact with the Bank Account Objects
"""
from math import trunc


class BankAccount:
    def __init__(self, account_number ,balance=0):
        self.account_number = account_number
        self.balance= balance
        print(f"{account_number} {balance}")
        enput = int(input("please chose form the menu: (1,2,3,4 or 5): \n "))
        self.enput = enput


    def deposit(self, new_deposit):

        new_deposit = int(input("Pls, how much ? \n "))



    def withdrawal(self):
        print("Withdrawal ")

    def balance_check(self):
       print("")

    def ops(self):
        if self.enput ==1:
            print( "you are asking for creating account ")
        elif self.enput ==2:
            print("your are asking for deposit ")
        elif self.enput ==3:
            print("your are asking for withdrawal ")
        elif self.enput ==4:
            print("you are asking for Check balance ")
        elif self.enput ==5:
            print("you are asking for Exit ")
        else :
            print("Wrong! input try again with a value in range 1 to 5 ")
    accounts = {}


    while True:
        print("1. Create account ")
        print("2. Deposit")
        print("3. Withdrawal")
        print("4. Check balance")
        print("5.Exit")

        break

account1 = BankAccount("")
account1.ops()
account1.deposit("")