l1=[]
n=int(input("Enter the no. of elements in the list: "))
for i in range(n):
    l1.append(int(input("Enter the element: ")))
print("The original list is: ",l1)
l2=[]
for i in range(n):
    if l1.count(l1[i])>1:
        continue
    else:
        l2.append(l1[i])
print("The unique elements are: ",l2)