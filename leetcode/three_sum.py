# 15. 3Sum

def threeSum(nums: list[int]) -> list[list[int]]:
    results = []
    
    nums.sort()
    
    def twoSum(nums, i, results):
        low, high = i + 1, len(nums) - 1
        
        while low < high:
            sum_3 = nums[i] + nums[low] + nums[high]
            
            if sum_3 < 0:
                low += 1
            elif sum_3 > 0:
                high -= 1
            else:
                results.append([nums[i], nums[low], nums[high]])
                low += 1
                high -= 1
                # If the next element of either low or high is the same as previous,
                # there will be duplicated answer. 
                while low < high:
                    if nums[low] == nums[low - 1]:
                        low += 1
                    if nums[high] == nums[high + 1]:
                        high -= 1
                    else:
                        break 
    
    # Start with a reference point, use twoSum method to find the other 2 points 
    # that sum to the opposite of the reference point. 
    for i in range(len(nums)):
        if nums[i] > 0:
            break 
        
        if i == 0 or nums[i-1] != nums[i]:
            twoSum(nums, i, results)
                        
    return results 
                        
                        
nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

nums = [0,0,0]
print(threeSum(nums))

nums = [-2,0,0,2,2]
print(threeSum(nums))