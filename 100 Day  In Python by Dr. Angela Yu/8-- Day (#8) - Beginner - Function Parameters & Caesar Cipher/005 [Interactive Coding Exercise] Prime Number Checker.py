def check_prime(n):
  """
  This function checks if a number is prime.

  Args:
    n: An integer number.

  Returns:
    True if the number is prime, False otherwise.
  """
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

prime_numbers = []
for num in range(1, 101):
  if check_prime(num):
    prime_numbers.append(num)

print("Prime numbers between 1 and 100:", prime_numbers)