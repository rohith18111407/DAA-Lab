# Python program for implementation of Radix Sort

"""Soorya sent this code"""
"""
def bubble_sort(arr, exp):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if (arr[j] // exp) % 10 > (arr[j + 1] // exp) % 10:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def radix_sort(arr):
    max_value = max(arr)
    exp = 1

    while max_value // exp > 0:
        bubble_sort(arr, exp)
        exp *= 10


# Example usage:
array = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(array)
print(array)
"""


# A function to do counting sort of arr[] according to
# the digit represented by exp.
"""
Radix Sort's time complexity of O(nd), where n is the size of the array and d is the number of digits in the largest number. It is not an in-place sorting algorithm because it requires extra space. Radix Sort is a stable sort because it maintains the relative order of elements with equal values.
"""

def countingSort(arr, exp1):

	n = len(arr)

	# The output array elements that will have sorted arr
	output = [0] * (n)

	# initialize count array as 0
	count = [0] * (10)

	# Store count of occurrences in count[]
	for i in range(0, n):
		index = (arr[i]/exp1)
		count[int((index)%10)] += 1

	# Change count[i] so that count[i] now contains actual
	# position of this digit in output array
	for i in range(1,10):
		count[i] += count[i-1]

	# Build the output array
	i = n-1
	while i>=0:
		index = (arr[i]/exp1)
		output[ count[ int((index)%10) ] - 1] = arr[i]
		count[int((index)%10)] -= 1
		i -= 1

	# Copying the output array to arr[],
	# so that arr now contains sorted numbers
	i = 0
	for i in range(0,len(arr)):
		arr[i] = output[i]

# Method to do Radix Sort
def radixSort(arr):

	# Find the maximum number to know number of digits
	max1 = max(arr)

	# Do counting sort for every digit. Note that instead
	# of passing digit number, exp is passed. exp is 10^i
	# where i is current digit number
	exp = 1
	while max1 // exp > 0:
		countingSort(arr,exp)
		exp *= 10

# Driver code to test above
arr = [ 170, 45, 75, 90, 802, 24, 2, 66]
radixSort(arr)

for i in range(len(arr)):
	print(arr[i],end=" ")

# This code is contributed by Mohit Kumra
# This code is updated by Sudeep Saxena(saxenasudeepcse@gmail.com) on July 9, 2020



