# 4. Looping over list
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
for letter in letters[0]:
    print(letter)
print("separate ")
# compare
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
for letter in letters[0:6]:
    print(letter)
print("separate ")
# Compare 01
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
for letter in letters[::2]:
    print(letter)

print("separate ")
#compare 02
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
for letter in letters[::-2]:
    print(letter)
print("separate ")
# Compare 03
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
for letter in letters[6: 9]:
    print(letter)

print("separate ")
print("separate ")

# Enumerate
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
for letter in enumerate (letters):
    print(letter[0], letter[1])
print("separate ")
print("separate ")
# Index, letter
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
for index, letter in enumerate (letters):
    print(index, letter)



