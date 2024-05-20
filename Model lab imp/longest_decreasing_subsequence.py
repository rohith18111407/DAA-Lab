"""
Input: arr[] = [15, 27, 14, 38, 63, 55, 46, 65, 85] 
Output: 3 
Explanation: The longest decreasing subsequence is {63, 55, 46} 
Input: arr[] = {50, 3, 10, 7, 40, 80} 
Output: 3 
Explanation: The longest decreasing subsequence is {50, 10, 7} 
"""

"""
The time complexity of the Dynamic Programming implementation of the Longest Decreasing Subsequence problem is O(n²)
"""

# Python 3 program to find the length of
# the longest decreasing subsequence

# Function that returns the length
# of the longest decreasing subsequence
def lds(arr, n):

	lds = [0] * n
	max = 0

	# Initialize LDS with 1 for all index
	# The minimum LDS starting with any
	# element is always 1
	for i in range(n):
		lds[i] = 1

	# Compute LDS from every index
	# in bottom up manner
	for i in range(1, n):
		for j in range(i):
			if (arr[i] < arr[j] and lds[i] < lds[j] + 1):
				lds[i] = lds[j] + 1

	# Select the maximum
	# of all the LDS values
	for i in range(n):
		if (max < lds[i]):
			max = lds[i]

	# returns the length of the LDS
	return max

# Driver Code
if __name__ == "__main__":
	
	arr = [ 15, 27, 14, 38, 63, 55, 46, 65, 85 ]
	n = len(arr)
	print("Length of LDS is", lds(arr, n))

# This code is contributed by ita_c
#time complexity = O(n*n)