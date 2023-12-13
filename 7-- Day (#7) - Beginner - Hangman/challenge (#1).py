# Challenge 1
# Step #1 - World List.
import random

word_list = ["Eslam", "Zead", "mouta"]

# TOdo-1
# Randomly chose a word from the word_list. and assign it to a Var called chosen_word.
import random
chosen_word = random.choice(word_list)

# TOdo-2
# Ask the user to guss a letter and assign it to a variable called Guss .make Guss lowercase
Guss = input("Guss the letter plz ").lower()
# TOdo-3
# Check if the letter the user guessed is in the chosen word_list words or not.
for letter in chosen_word:
    if letter == Guss:
        print("Right letter ")
    else:
        print("Wrong entry!")

