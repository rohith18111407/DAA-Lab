def count_inversion1(nums):
    count=0
    for i in range(1,len(nums)):
        for j in range(i,-1,-1):
            if(nums[i]<nums[j]):
                count+=1
    return count

nums=[7,8,3,1,5]
print("Entered list:\n ",nums)
print("\nNo. of iversions in the list: ",count_inversion1(nums),"\n")