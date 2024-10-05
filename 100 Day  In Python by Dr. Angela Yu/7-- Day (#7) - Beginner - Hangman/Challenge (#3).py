# Compeleting our challenge
import random

word_list = ["ahmed", "zeaad", "eslam"]
chosen_word = random.choice(word_list)
print(chosen_word)

display = []
Word_lenght = len(chosen_word)
for _ in range(Word_lenght):
    display += "_"
    print(display)

end_of_game = False

while not end_of_game:
    Guss = input("Guss a letter     ").lower()
    for position in range(Word_lenght):
        letter = chosen_word[position]
        if letter == Guss:
            display[position] = letter
    print(display)
if "_" not in display:
    end_of_game = True
    print("WOW, You Just Win!")
