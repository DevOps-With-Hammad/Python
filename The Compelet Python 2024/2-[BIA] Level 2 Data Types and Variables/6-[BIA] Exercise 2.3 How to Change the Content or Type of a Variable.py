# 6. [BIA] Exercise 2.3 How to Change the Content or Type of a Variable

"""
Ali is 1.65 meters tall , sara is 1.09 meters tall.
1. Create variable as string and call it "Height"
2. Assign the Height a value = 1.09.
3. Print the Height of sara.
4. change the Height data string to float .
5. add 0.66 to 1.09.
6. print the new height
"""
Ali = 1.65
Sara = 1.09
Height = "1.09"
print(Sara)
ch_height = float(Height)
new_height = ch_height + 0.66
print(new_height)





# Given:
# Ali is 1.65 meters tall and Sara is 1.09 meters tall.

# 1. Create a variable as a string and call it "Height"
Height = "1.09"  # Assign the value "1.09" as a string

# 2. Print the Height of Sara
# Since Sara's height is stored in a separate variable, we print it directly.
Sara = 1.09
print(Sara)  # Output: 1.09

# 3. Change the Height data type from string to float
ch_height = float(Height)  # Convert string "1.09" to float 1.09

# 4. Add 0.66 to Sara's height
new_height = ch_height + 0.66  # 1.09 + 0.66 = 1.75

# 5. Print the new height
print(new_height)  # Output: 1.75
