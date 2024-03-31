class Phone :
    def __init__(self, app, games, other):
        self.app = app
        self.games = games
        self.other = other

User_1  = Phone("Facebook", "Snake", "System")
User_2 = Phone("WHats app", "Cat", "System")
User_3  = Phone("Instagram", "Basket", "System")
User_4  = Phone("Twitter", "Ball", "System")

print(User_1.app, User_1.games, User_1.other)
print(User_3.games)
print(User_2.other)