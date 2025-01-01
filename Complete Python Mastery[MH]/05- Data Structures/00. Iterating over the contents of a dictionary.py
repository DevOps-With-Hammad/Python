# Iterating over the contents of a dictionary
#01
file_counts = {"jpg": 10, "txt": 14, "csv": 12, "py":23}
for extension in file_counts:
    print(extension)
# 02this printout the extension of the files

file_counts = {"jpg": 10, "txt": 14, "csv": 12, "py":23}
for ext, amount in file_counts.items():
    print("There are:{} files with .extension {}".format(amount, ext))

#03
print(" separate line ")
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts.keys())# this is to print the key str of the dict meaning the first part of the dict
print(file_counts.values())# this is to print the value of the dict meaning the second part of the dict

# dict_keys(['jpg', 'txt', 'csv', 'py'])
# dict_values([10, 14, 2, 23])
print("")
print("")
print("")
print("")

#04
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for value in  file_counts.values():
# meaning the iteration will go through the value of the dict >> second part
   print(value) # 10 14 2 23 in a column


print("")
print("")

# 05
def count_letters(text):
    result= {}
    for letter in text:
        if letter not in result:
            result[letter]= 0
        result[letter] +=1
    return result

print(count_letters("abcdefg"))
print(count_letters("are you mad really "))








