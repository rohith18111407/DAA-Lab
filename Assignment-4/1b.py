from hypothesis import given
from hypothesis.strategies import lists, integers

# correctcode

def count_inversions(nums):
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] > nums[j]:
                count += 1
    return count

#incorrect code

def count_inversions2(nums):
    nums.sort()
    count = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            count += 1

    return count

# hypo test

@given(lists(integers()))
def test_inversions(nums):
    assert count_inversions(nums) == count_inversions2(nums)

test_inversions()