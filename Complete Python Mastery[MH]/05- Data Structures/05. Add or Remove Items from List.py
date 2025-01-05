# Add or Remove Items from List.
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
# Add elements to the list
letters.append("d") # add element to the end of the list .
print(letters)
letters.insert(6, "-") # adding elements to specific position
print(letters)


# Remove element for list
letters.pop(3) # remove element that have index 3
print(letters)
letters.remove("F") # remove a specified element in list
print(letters)
del letters[0:3] # del elements from index [0:3]
print(letters)

