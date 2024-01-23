def prime_checker(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


prime_number = []
for num in range(1, 100):
    if prime_checker(num):
        prime_number.append(num)

print("prime number between 1 to 100 is going to be  ", prime_number)
