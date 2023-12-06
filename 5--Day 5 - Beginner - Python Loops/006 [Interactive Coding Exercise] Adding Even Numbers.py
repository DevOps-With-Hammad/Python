# calculating all the even numbers from 1 to 100 including them
total = 0
for nums in range(2, 101, 2):
    # print(nums)
    total += nums
    print(total)
total2 = 0
for Num in range(1, 101):
    if Num % 2 == 0:
        total2 += Num
print(f"Here is the same output with new way to sole the problem \n {total2}")
