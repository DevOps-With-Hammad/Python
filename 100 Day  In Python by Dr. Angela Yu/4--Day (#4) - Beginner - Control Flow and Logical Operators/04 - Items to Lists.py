# 004 the offset and appending Items to Lists
countries_of_africa = ["Egy", "Libiya", "Tunisa", "Moraco", "Togo", "Algeria", "Libnon"]
# adding more than one element in one list
countries_of_africa[1] ="Nigeria", "togog", "nibal"
# Adding 2 elements in one list
countries_of_africa[2] ="Nigeria", "togog"
# adding one element in one list
countries_of_africa[3] ="Nigeria"

countries_of_africa

print(countries_of_africa)

# append to add single Item at the end of list
countries_of_africa.append("Englaaaaand")
print(countries_of_africa)

# Data Structure , More In list.
# list.append() == >> add an item at the end of list
countries_of_africa.append("Turkey")
print(countries_of_africa)

#List.extend() == >>  Extend the lsit by appending all the items from the iterable.
#countries_of_africa.extend("Ymaha", "Yakoza")
countries_of_africa.extend(["Ymaha", "Akashy", "Yandel"])
print(countries_of_africa)

#List.insert() == >>  insert an Item at a given position .
#countries_of_africa.extend("Ymaha", "Yakoza")
countries_of_africa.insert(0, "Egypt")
print(countries_of_africa)

#List.count() == >>  return the Number of times X appears in list.
#countries_of_africa.extend("Ymaha", "Yakoza")
x = countries_of_africa.count("Egy")
print(x)







