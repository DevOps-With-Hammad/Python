# What is a dictionary
x = {}
print(type(x))# <class dict
y = ()
print(type(y)) # <class Tuple
z = []
print(type(z)) # <class List


file_counts = {"Jpg": 10 , "txt":14, "csv": 2, "py": 23  }
print(file_counts)

file_counts["cfg"] = 9
print(file_counts)
del file_counts["Jpg"]
print(file_counts)