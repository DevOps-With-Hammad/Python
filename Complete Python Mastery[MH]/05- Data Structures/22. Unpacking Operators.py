# Unpacking Operator
numbers = [1, 2, 3, 4, 5, 6] # [1, 2, 3, 4, 5, 6]
print(numbers)

numbers = (1, 2, 3, 4, 5, 6)# (1, 2, 3, 4, 5, 6)
print(numbers)

print(*numbers)# 1 2 3 4 5 6

values = list(range(5))

print(values) # [0, 1, 2, 3, 4]

values = [*range(5), *"Hammad" ]
print(values) # [0, 1, 2, 3, 4, 'H', 'a', 'm', 'm', 'a', 'd']
# Unpacking lists and combining them again .

lis01 = [1, 2 ]
lis02 = [5]
val_lis00 = [*lis01, *lis02]
print(val_lis00) # [1, 2, 5]

# Unpacking dicts

dic01 = {"Hammad" : 12}
dict02 = {"Hamza": 10 , "Hady": 2 }
print(dic01, dict02)
combined_dicts = {**dic01, **dict02, "Hana ": 12}
print(combined_dicts)

