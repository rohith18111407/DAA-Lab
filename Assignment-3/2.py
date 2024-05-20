def comparison_count_sort(nums):
    count = [0] * len(nums)
    nums_sorted = [0] * len(nums)
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                count[i] += 1
            elif nums[i] < nums[j]:
                count[j] += 1
    for i in range(len(nums)):
        nums_sorted[count[i]] = nums[i]
    for i in range(len(nums_sorted)):
        if nums_sorted[i]==0:
            nums_sorted[i]=nums_sorted[i-1]
    return nums_sorted
print(comparison_count_sort([11,2,4,1,11,5,6,77,6,4,-1])) 