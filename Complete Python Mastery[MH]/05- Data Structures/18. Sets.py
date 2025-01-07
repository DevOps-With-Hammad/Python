#18.Sets
from enum import unique

values = [1, 2, 3, 4, 6 ]
uniques = set(values)
second = {1, 6 }
second.add(5)
second.remove(1)
print(second)
print(uniques)
first = set(values)
second = {1, 5, 7, 9}
print("| >>> ",first | second)
print("& >>>",first & second)
print("- >>>",first - second)
print("^ >>>",first ^ second )

