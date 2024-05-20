#Function for performing insertion sort
def insertionSort(arr):
    if(len(arr)<=1):
        return 
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key


# Function to return K'th smallest
# element in a given array
def kthsmallest(arr,k):
    insertionSort(arr)
    return arr[k-1]


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