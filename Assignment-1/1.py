import random

def generate(n):
    arr = []    
    max = 1000
    for i in range(n):  
        num = random.randint(1,max)
        while num in arr :
            num = random.randint(1,max)
        arr.append(num)
    arr.sort()
    return arr

def main():
    n = int(input("Enter the value of n: "))
    arr = generate(n)
    print(arr)

main()