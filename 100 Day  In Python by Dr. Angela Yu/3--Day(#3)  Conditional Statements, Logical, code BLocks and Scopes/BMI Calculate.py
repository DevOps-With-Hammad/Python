# BMI simple calculate.

# First setting our Vars
weight = float(input("Please Enter your weight here, in meters pls \n  "))
height = float(input("please Enter your height here, in kg please \n  "))
# Define BMI
# We can use a round function to round it to the nearest number like this :
bmi = round(weight / (height ** 2))
# Here is the part of if function to declare results (Underweight- normal weight- overweight-  obese- clinically obese)
if bmi < 18.5:
    print(f"your BMI is {bmi}, \n under weight ")
elif bmi < 25:
    print(f"your BMI is {bmi}, \n Normal weight ")
elif bmi < 30:
    print(f"Your BMI is {bmi}, \n Over weight ")
elif bmi < 35:
    print(f"Your BMI is {bmi}, \n  Obese ")
else:
    print(f"Your BMI is {bmi}, clinically obese ")
