# # List Comprehension Examples
# Create a list of tuples where each tuple contains the numbers 1, 2, and 3.
numbers = [(1, 2, 3) for _ in range(5)]
print(numbers)
### Simple List Comprehension
print("List comprehension result:")

# The following list comprehension compacts several lines 
# of code into one line:
print([x*2 for x in range(1,11)])

### Long form for loop
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code shown below:
my_list = []
for x in range(1,11):
    my_list.append(x*2)
print(my_list)

print("List comprehension result:")
print([x for x in range(1,101) if x % 10 == 0])



filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
[x for x  in filenames if "." in x newfilenames =x.split(".")[0][1]  ]

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
# The list comprehension above accomplishes the same result as
# the long form version of the code:
print("Long form code result:")
my_list = []
for x in range(1,101):
    if x % 10 == 0:
        my_list.append(x)
print(my_list)

def squares (start, end ):
    return [x**2 for x in range (start,end+1)]

print(squares(2,3))
print(squares(1,5))
print(squares(0, 10))
ll = 6
zz = ll**2
print(zz)
# List Operations and Methods
