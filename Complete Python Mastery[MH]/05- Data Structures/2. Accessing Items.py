# 2. Accessing Items
letters = ["a", "b", "c", "d"]
letters[0:2] = "A","B","C"
print(letters[0:3])
print(letters)

# using list range to print even numbers
numbers = list(range(100))
print(numbers[::10]) # in a forward order
print(numbers[::-10]) # in reverse order

