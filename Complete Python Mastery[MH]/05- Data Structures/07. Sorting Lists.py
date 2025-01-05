# 07. Sorting Lists
numbers= [3, 15, 10, 6, 26, 3, 12]
numbers.sort()
print(numbers) # Sorting

words = ["Isuzu", "Ford", "D-max", "Honda", "Toyota"]
print(words.sort())

# Reverse order
numbers= [3, 15, 10, 6, 26, 3, 12]
numbers.sort(reverse=True)
print(numbers) # Sorting in reverse order

values= [13, 6, 9, 12, 5, 4, 20, 100, 0, 102]
print(sorted(values))

# do the sort on list of Items

items = [("Product01", 10),
         ("Product02", 9),
         ("Product03", 13)]
items.sort()
print(items)
print(" Separator ")
def sort_item(item):
    return  item[1]
items.sort(key=sort_item)
print(items)


# happy coding