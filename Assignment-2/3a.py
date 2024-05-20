str=input("Enter the string: ")
l1=list(str)
l2=[]
for i in range(len(l1)):
    l2.append(l1.count(l1[i]))
max=max(l2)
l3=[]
for i in range(len(l2)):
    if (max==l2[i] and l1[i] not in l3):
        l3.append(l1[i])
print("The list is: ",l3)