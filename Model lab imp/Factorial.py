"""
For both the iteration and recursion solution, the time complexity of the factorial program is O(n), where n = number.
"""

# Python 3 program to find
# factorial of given number

# Function to find factorial of given number
def factorial(n):
	
	res = 1
	
	for i in range(2, n+1):
		res *= i
	return res
# Driver Code
num = 5
print("Factorial of", num, "is",
factorial(num))
