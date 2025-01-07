# 12 Zip function
list1 = [1,2,3]
list2 = [10, 20, 30]
# how to combine these 2 lists like that [(1, 10), (2, 20), (3, 30)]
print(list(zip(list1, list2))) # it takes one or more iterable so we don't have to pass a list here
print(list(zip("CEO",list1, list2))) # in python you can do it in a single line

# happy coding
