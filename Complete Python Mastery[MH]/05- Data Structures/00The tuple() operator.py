# The tuple() operator

# convert a list to a tuble
my_list = [1, 2, 3, 4 ]
my_tuble = tuple(my_list)
print(my_tuble)

my_tuble01 = 1,2,3,4,5,6,7,9
print(my_tuble01)

# Tuples with mutable objects
# A tuple with a list as an element
my_tuple = (1, 2, ['a', 'b', 'c'])
my_tuple[2][0] = 'x'
print(my_tuple)  # Outputs: (1, 2, ['x', 'b', 'c'])


# Returning multiple values from functions
def calculate_numbers(a,b):
    return  a+b, a*b , a-b, a/b

result = calculate_numbers(10, 2 )
print(result)
#
def calculate_numbers01(a,b):
    return  a+b , a-b , a*b, a/b

add_result, sub_result, mul_result, di_result = calculate_numbers01(10,5 )

print(add_result)


