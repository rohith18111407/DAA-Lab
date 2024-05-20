import random

def generate(n):
    arr = []    
    max = int(input("Enter the max limit of range for random numbers of value n = ",n))
    for i in range(n):  
        num = random.randint(1,max)
        while num in arr :
            num = random.randint(1,max)
        arr.append(num)
    return arr

def main():
    for i in range(4):
        n = int(input("Enter the value of n: "))
        arr = generate(n)
        print("The randomly generated array is: ",arr,"\n")

        print("----- Insertion sort -----")
        new_arr=insertion(arr)
        print("After insertion sort: ",new_arr,"\n")
        print("----- Shell sort -----")
        new_arr=shell(arr)
        print("After Shell sort: ",new_arr,"\n")
        print("----- Radix exchange sort -----")
        new_arr=radix(arr)
        print("After Radix exchange sort: ",new_arr,"\n")


#insertion sort-------------------------------
def insertion(arr):
    n=len(arr)
    for i in range(1,n):
        j=i-1
        key=arr[i]
        while(j>=0 and key<arr[j]):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr


#shell sort-------------------------------------
def shell(arr):
    n1=len(arr)
    interval=n1//2
    while interval>0:
        for i in range(interval,n):
            temp=arr[i]
            j=i
            while j>interval and arr[j-interval]>temp:
                arr[j]=arr[j-interval]
                j-=interval
            arr[j]=temp
        interval//=2
    return arr


#radix sort------------------------------------------
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
    #  position of this digit in output array
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
def radix(arr):
 
    # Find the maximum number to know number of digits
    max1 = max(arr)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 // exp > 0:
        countingSort(arr,exp)
        exp *= 10

main()