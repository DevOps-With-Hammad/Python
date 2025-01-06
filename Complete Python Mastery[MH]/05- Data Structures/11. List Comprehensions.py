# 11. List Comprehensions * vital topic *
items = [("Product 01 ", 10),
         ("Product 02 ", 9),
         ("Product 03 ", 12)

]
price = [item[1] for item in items]
filterd= [item for item in items if item[1] >= 10]
print(price)
print(filterd)

teacher_names = {"Math": "Aniyah Cook", "Science": "Ines Bisset", "Engineering": "Wayne Branon"}
print(teacher_names.values())

animal = "Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])