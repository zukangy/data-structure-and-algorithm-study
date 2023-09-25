# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# This is a O(nlogn) solution as it uses the sorting algorithm; adopted from standard solution

def longestConsecutive(nums: list[int]) -> int:
    
    # If the list is empty, return 0
    if not nums:
        return 0 
    
    # this algorithm requires a sorted array
    nums.sort()
    
    current_longest_length = 1
    longest_length = 1 
    
    for i in range(1, len(nums)):
        # If nums[i] == nums[i-1], nothing will happen
        if nums[i] != nums[i-1]:
            # Check the current number and its previous number
            if nums[i] == nums[i-1] + 1:
                current_longest_length += 1 
            else:
                longest_length = max(longest_length, current_longest_length)
                current_longest_length = 1
                
    # If the last number is also in the sequence, the else condition won't see it
    longest_length = max(longest_length, current_longest_length)
    return longest_length


inputs = [[100,4,200,1,3,2], [0,3,7,2,5,8,4,6,0,1]]

for i in inputs:
    print(longestConsecutive(i))