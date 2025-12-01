"""
Exercise 3: Squares of Even/Odd Numbers
1. Create a Python script that prints the squares of all even or odd numbers within the range of 100 to 200. Choose either even or odd numbers and document your choice in the code. 

"""


for i in range(100,201):
  if i%2==0:
    print(f"{i} is even number and its's square is: {i**2}")
print("*"*100)
for i in range(100,201):
  if i%2!=0:
    print(f"{i} is odd number and it's square is: {i**2}")
    
# Time Complexity: O(1) , Precise TC : O(100) + O(100) , so it is constant.
# Space Complexity: O(1)