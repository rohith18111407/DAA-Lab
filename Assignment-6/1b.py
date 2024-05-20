# Python3 implementation of QuickSort
 
# Function to find the partition position
def partition(array, low, high):
 
    # Choose the rightmost element as pivot
    pivot = array[high]
 
    # Pointer for greater element
    i = low - 1
 
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with
    # e greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# Function to perform quicksort
def quick_sort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quick_sort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, high)


# Function to return K'th smallest
# element in a given array
def kthsmallest(arr,k):
    quick_sort(arr,0,len(arr)-1)
    return arr[k-1]
 
 
# Driver code
if __name__=='__main__':
    arr=[]
    n=int(input("Enter the number of elements: "))
    for i in range(n):
        arr.append(int(input("Enter the element: ")))
    print("\nEntered array: ",arr)
    k=int(input("\nEnter the k value: "))
    val=kthsmallest(arr,k)
    print("\nSorted array: ",arr)
    print("\n",k,"th smallest value is: ",val)