# 09. Map Function
items = [("Product 01 ", 10),
         ("Product 02 ", 9),
         ("Product 03 ", 12)

]
price = []
for item in items :
    price.append(item[1])

print(price)

# doing that using map function
items = [("Product 01 ", 10),
         ("Product 02 ", 9),
         ("Product 03 ", 12)

]
prices =list (map(lambda item:item[1], items))
print(prices)