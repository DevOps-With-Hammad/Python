# Scoping using If with  or without function
from typing import List

game_level = 3


def create_enemy():
    enemys = ["cars", "Bus", "Trains"]
    if game_level < 5:
        New_enemy = enemys[0]
    print(New_enemy)
