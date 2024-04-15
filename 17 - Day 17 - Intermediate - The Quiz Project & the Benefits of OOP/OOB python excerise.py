# OOB in Action
"""
declare a class in python using OOB
"""
class User:
    def __init__(self, User_ID, Usr_name):
        self.userid =User_ID
        self.username = Usr_name
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers +=1
        self.following +=1



User_1 = User("001", "Hammad ")
User_2 = User("002", "ahmed ")
User_3 = User("003", "Zead")
User_4 = User("004", "Eslam ")

User_1.follow(User_2)
print(f"here is the user 1 date {User_1.follow}")