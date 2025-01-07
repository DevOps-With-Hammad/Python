# 20. Dictionary Comprehensions

value = []
for x in range(5):
    x+=1
    value.append(x*2)# (2, 4, 6, 8, 10)
print(value)

xvalue = [x*2 for x in range(1,6) ]
print(xvalue)

#
primary = [x for x in range(2, 101) if all (x % i !=0 for i in range (2, int(x**0.5)+1))]
print(primary)
# primary number in python