"""
Input: arr[] = {8, 4, 2, 1}
Output: 6
Explanation: Given array has six inversions:
(8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1).

Input: arr[] = {3, 1, 2}
Output: 2
Explanation: Given array has two inversions:
(3, 1), (3, 2) 
"""

# Python3 program to count inversions
# in an array
def getInvCount(arr, n):
	inv_count = 0
	for i in range(n):
		for j in range(i + 1, n):
			if (arr[i] > arr[j]):
				inv_count += 1

	return inv_count

# Driver Code
arr = [1, 20, 6, 4, 5]
n = len(arr)
print("Number of inversions are",getInvCount(arr, n))
# This code is contributed by Smitha Dinesh Semwal
