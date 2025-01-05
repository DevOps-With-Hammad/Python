# 10 . Filter function
items = [("Product 01 ", 10),
         ("Product 02 ", 9),
         ("Product 03 ", 12)

]

x= list (filter(lambda item:item[1]>= 10, items))
print(x)