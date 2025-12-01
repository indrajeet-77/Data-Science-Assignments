""" 
Exercise 2: Product of Random Numbers

1. Develop a Python program that generates two random numbers and asks the user to enter the product of these numbers. The program should then check if the user's answer is correct and display an appropriate message.

"""

import random
def random_num_gen():
  n1=random.randint(1,100)
  n2=random.randint(1,100)
  return [n1,n2]

nums=random_num_gen()
print(f"What is the product of {nums[0]} and {nums[1]} " )
prod=int(input("Enter the product:"))
if prod==nums[0]*nums[1]:
  print("Your answer is correct")
else:
  print("Your answer is incorrect")

# Time Complexity : O(1)
# Space Complexity : O(1)