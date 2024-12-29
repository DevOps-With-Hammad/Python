# 12. Exercise

def fizz_buzz(value):
    value=int(input("your value is : "))
    if value % 3 == 0 and value % 5 == 0:
        print("fizz Buzz")
    elif value %5 ==0:
        print("buzz")
    elif value %3 ==0:
        print("fizz")
    else:
        print("Wrong Entry ")
while fizz_buzz(value="")is True:
    continue
fizz_buzz(15)