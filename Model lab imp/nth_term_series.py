# Python 3 program to find
# n-th term of
# series 1, 3, 6, 10, 15, 21...

	
# Function to find the
# nth term of series
def term(n) :
	# Loop to add numbers
	ans = 0
	for i in range(1,n+1) :
		ans = ans + i
	
	return ans


# Driver code
n = 4
print(term(n))

# This code is contributed
# by Nikita Tiwari.
