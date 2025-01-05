# List Unpacking .

number = [1, 2, 3, 4, 5, 6, 7, 9]
# first, second, third, fourth = number
# ValueError: too many values to unpack (expected 4)
# to avoid that we do
first, second, third, *other, last,  = number
print(second) # 2
print(other) # [4, 5, 6, 7]
print(first, last ) # 1 9
print(other) # [4, 5, 6, 7]




