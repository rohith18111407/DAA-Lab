#Python program to find the largest sum of all subsets in the list

#Divide and conquer strategy to find the contiguous subsets
#in the list A and storing it in A1
def Divide_and_Conquer_sublist(A,A1):
    l=len(A)
    if l>=2:
        mid=l//2
        left_list=[]
        for i in range(mid):
            left_list.append(A[i])
        A1.append(left_list)
        
        right_list=[]
        for i in range(mid,l):
            right_list.append(A[i])
        A1.append(right_list)
        
        Divide_and_Conquer_sublist(left_list,A1)
        Divide_and_Conquer_sublist(right_list,A1)

#Divide and conquer strategy to find the max element
#in A1 by providing starting index and length of A1
def Divide_and_Conquer_findmax(A1,index,length):
    max=-1
    if(length-1==0):
        return A1[index]
    if(index>=length-2):
        if(A1[index]>A1[index+1]):
            return A1[index]
        else:
            return A1[index+1]
    max=Divide_and_Conquer_findmax(A1,index+1,length)
    if(A1[index]>max):
        return A1[index]
    else:
        return max

#Function to calculate the sum of elements in 
#each subset of list A1
def calc_sum(A1):
    for i in range(len(A1)):
        sum=0
        for j in range(len(A1[i])):
            sum+=A1[i][j]
        A1[i]=sum

#Driver code
A=[]
n=int(input("Enter the no. of elements in the list: "))
print()

#Getting input list
for i in range(n):
    A.append(int(input("Enter the value: ")))

print("\nEntered List: \n",A,"\n")

A1=[]
Divide_and_Conquer_sublist(A,A1)
print("Sublists in the list: \n",A1,"\n")

calc_sum(A1)
print("Sum of each sublist: \n",A1)        

max=Divide_and_Conquer_findmax(A1,0,len(A1))
print("\nMaximum element: ",max,"\n")
