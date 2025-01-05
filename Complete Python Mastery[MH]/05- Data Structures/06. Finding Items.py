# Finding Items
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
print(letters.index("I")) # 8
if "D" in letters:
    print(letters.index("D"))
else:
    print("Not found ")

# to make the search more public and accurate
char = "Z"
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
print(letters.index("I")) # 8
if char in letters:
    print(letters.index(char))
else:
    print("Not found ")


#

char = "H"
letters =["A", "B", "C", "D", "E", "F", "G", "H", "I"]
try:
    print(letters.index(char))
except ValueError:
    print("Not found ")
