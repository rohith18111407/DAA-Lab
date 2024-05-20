def maximum(low,high,arr):
    if low==high:
        return arr[low]
    else:
        mid=(low+high)//2
        leftmax=maximum(low,mid,arr)
        rightmax=maximum(mid+1,high,arr)
        return max(leftmax,rightmax)

l=[39,38,69,72,67,70]
max_val=maximum(0,len(l)-1,l)
print("List: ",l)
print("Maximum value in the list: ",max_val)