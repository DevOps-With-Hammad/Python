# 08. Lamda Function
items = [("Product 01 ", 10),
         ("Product 02", 9 ),
         ("Product 03 ", 12)

]

def sort_item(item):
    return  item [1]

items.sort(key=sort_item)
print(items)
print("Separator ")
#
items = [("Product 01 ", 10),
         ("Product 02", 9 ),
         ("Product 03 ", 12)

]

items.sort(key=lambda item:item[1])
print(items)

# Happy coding

