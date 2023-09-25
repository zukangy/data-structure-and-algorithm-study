# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


def getResult(nums):
    l = len(nums)
    
    left_prod, right_prod, ans = [1] * l, [1] * l, [1] * l  
    
    # Skip the first element as there is no elements at the left of nums[0]
    # The ith element of left_prod is the product of the (i-1)th element in nums 
    # and the (i-1)th element in the left_prod
    for i in range(1, l):
        left_prod[i] = nums[i - 1] * left_prod[i - 1]
        
    # Skip the last element as there is no elements at the right of nums[l-1]
    # Same reasoning as above
    for i in reversed(range(l-1)):
        right_prod[i] = nums[i + 1] * right_prod[i + 1]
        
    for i in range(l):
        ans[i] = left_prod[i] * right_prod[i]
    
    return ans 


inputs = [[1,2,3,4], [-1,1,0,-3,3]] 

for i in inputs:
    print(getResult(i))