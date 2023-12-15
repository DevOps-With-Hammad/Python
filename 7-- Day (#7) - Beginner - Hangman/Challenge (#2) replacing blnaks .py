import random

word_list = ["Ahmed", "Zeaad", "Eslam"]
chosen_word = random.choice(word_list)
print(chosen_word)

display = []
Word_lenght = len(chosen_word)
for _ in range(Word_lenght):
    display += "_"
    print(display)
Guss = input("Guss a letter     ").lower()
for position in range(Word_lenght):
    letter = chosen_word[position]
    if letter == Guss:
        display[position] = letter
print(display)

