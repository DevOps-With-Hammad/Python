# 14. [IGA] Creating Advanced Functions (Keyword and Default Values)
name = input("what is your name ? ")
age = input(f"what is {name}'s age ? ")

def age_in_one_year(name, age):
    age_next_year= int(age) + 1
    print(f"in one year {name} will be {str(age_next_year)} Year old ")

age_in_one_year(name, age)
age_in_one_year("Adam", 1)
age_in_one_year("Barraa", 25)
