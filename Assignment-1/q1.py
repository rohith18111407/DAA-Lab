import random
from time import time
import numpy as np
import matplotlib.pyplot as plt

def generate(n,max):
    arr = []
    for i in range(n):
        num = random.randint(1,max)
        while num in arr :
            num = random.randint(1,max)
        arr.append(num)
    return arr

def insort(arr,size):
    for i in range(size):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = temp
    return arr
    
def shellsort(arr,size):
    gap = size//2
    while(gap >= 1):        
        for j in range(gap,size,1):
            k = j - gap
            while k >= 0:
                if(arr[k] > arr[k+gap]):
                    arr[k],arr[k+gap] = arr[k+gap],arr[k]
                else: 
                    break
                k = k-gap
        gap = gap//2

def radixsort(arr,size):
    loop_size = len(str(max(arr)))
    for i in range(loop_size):
        buckets = [ [] for i in range(10)]
        for j in range(size):
            dig = digit(arr[j],i+1)            
            buckets[dig].append(arr[j])
        arr = []
        for k in range(len(buckets)):
            arr = arr + buckets[k]        
    return arr
      
def digit(num,place):
    for i in range(place-1):
        num = num//10
    return num%10
    
def main():
    #n = int(input("Enter number of values : "))
    times = []
    arr = generate(10,100)     
    init = time()
    arr = insort(arr,len(arr))   
    times.append(int(round((time() - init * 1000))))
    arr = generate(100,1000)
    init = time()         
    arr = insort(arr,len(arr))
    times.append(int(round((time() - init * 1000))))
    arr = generate(1000,10000)
    init = time()     
    arr = insort(arr,len(arr))   
    times.append(int(round((time() - init * 1000))))
    arr = generate(10000,100000)
    init = time()     
    arr = insort(arr,len(arr))   
    times.append(int(round((time() - init * 1000))))
    arr = generate(100000,1000000)
    init = time()     
    arr = insort(arr,len(arr))   
    times.append(int(round((time() - init * 1000))))
    x = [10,100,1000,10000,10000]
    plt.plot(x,time)
    plt.show()


main()


