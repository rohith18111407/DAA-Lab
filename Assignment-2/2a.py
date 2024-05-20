n=int(input("Enter the value of n: "))
sum=0
for i in range(1,n+1):
    for j in range(1,i+1):
        sum+=j
        print(j,"+",end=" ")
print("\nThe sum is: ",sum)