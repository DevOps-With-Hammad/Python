# 5. [BIGA] Level 5 Final Exercise Grocery Shopping List

"""
# Your code start here .
- step 01 : create the initial shopping list .
- step 02 : add apple to the list
-Step 03 :remove bread form the list
-step 04 :create the show list function
"""
shopping_list = ["Banana ", "Suger", " rice ", "bread ", " soda "]
print(f" Here is my shopping list: {shopping_list}")
shopping_list.append("apple")
print(shopping_list)
shopping_list.remove(shopping_list[3])
print(f"shopping list after removing bread and adding apple:  {shopping_list} ")