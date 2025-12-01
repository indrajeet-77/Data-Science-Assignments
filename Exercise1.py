""" 
Exercise 1: Prime Numbers
Write a Python program that checks whether a given number is prime or not. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

"""

def isprime(num:int)->bool:
  if num <=1:
    return False
  for i in range(2,int(num**0.5)+1):
    if num%i==0:
      return False
  else:
      return True

number=int(input("Enter the number : "))
answer=isprime(number)
if answer:
  print(f"{number} is a prime number")
else:
  print(f"{number} is not a prime number")
  
  
# Time Complexity : O(N**0.5) or O(Square root of N)
# Space Complexity : O(1)
  