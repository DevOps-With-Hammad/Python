# 004 [Interactive Coding Exercise] Paint Area Calculator
# here is our code
import math
print("Welcome to, the paint wall calculator! \n Plz  fill out the requirements fields \n ")
def paint_cal(height, width, cover):
    area = height * width
    Num_of_can =math.ceil( area / cover)
    print(f"You'll Need\n ({Num_of_can})Can of Paint")


test_h = int(input("Height of wall : "))
test_w = int(input("Width of wall : "))
covrage = 5
paint_cal(height=test_h, width=test_w, cover=covrage)