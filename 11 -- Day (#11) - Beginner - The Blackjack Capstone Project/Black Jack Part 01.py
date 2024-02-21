# 003 Hint 4 & 5 Solution Walk through.
print(" Welcome to Jack Black V1")

""""
Importing the Random Module
"""
import random

def cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    random.choice(cards)
    return card


User_cards = []
COm_cards = []

for _ in range(2):
    User_cards.append = (deal_cards())
    COm_cards.append = (deal_cards())


def cards_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and cards > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
