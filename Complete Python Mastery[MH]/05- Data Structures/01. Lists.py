# 01.Lists
letters = ["a", "b", "c", ] # this is a list of letters
matrix = [[1, 2], [3, 5]] # This is 2 Dimension list
print(matrix) # this iss how to print the matrix .
print(matrix[0])# This How to print the first Dimension matrix.
print(matrix[1]) # printing the second dimension of the matrix.

# also you can declare a matrix and multiply it by a given value like that
mat = [[2, 3]]* 3
print(mat)# This Multiplication is to repeat the elements not do the actual  math operation.

################
def difference(x, y):
    z = x - y
    return z


print(difference(5, 3))