# 21. Generator Expressions
from sys import  getsizeof
values = [x *2 for x in range (9)]  # this is considered as list
for x in values:
    print(x)


print("**** *** **  Separator ** ** ** ** ")
value = (z*2 for z in range(100)) # generator object <genexpr
for z in value :
  print(z)

print(" Size of block is : ", getsizeof(value))