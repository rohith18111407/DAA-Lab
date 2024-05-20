import random

def generate(n):
    arr = []    
    max = int(input("Enter Max limit : "))
    for i in range(n):  
        num = random.randint(1,max)
        while num in arr :
            num = random.randint(1,max)
        arr.append(num)
    arr.sort()
    return arr

def binary(arr,val):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        if (arr[mid] == val):
            return mid
        elif (arr[mid] < val):
            start = mid + 1
        else:
            end = mid - 1
    return -1

def binary_recursive(arr,val,start,end):
    if(start > end):
        return -1
    else:
        mid = (start + end)//2  
        if(arr[mid] == val):
            return mid
        elif(arr[mid] < val):
            return binary_recursive(arr,val,mid+1,end)
        else:
            return binary_recursive(arr,val,start,mid-1)

def main():
    n = 10
    arr = generate(n)
    print(arr)
    val = int(input("Enter value to search : "))
    print(binary_recursive(arr,val,0,len(arr)-1))

main()


