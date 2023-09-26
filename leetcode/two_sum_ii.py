# 167. Two Sum II - Input Array is Sorted

# Find the indices of the two numbers in the array adding up to target. 
def twoSum(numbers, target):
    if len(numbers) == 2:
        if sum(numbers) == target:
             return [1, 2]
         
    length = len(numbers)
    
    i = 0
    j = length - 1
    while i < j:
        if numbers[i] + numbers[j] > target:
            j -= 1
        elif numbers[i] + numbers[j] < target:
            i += 1
        else:
            return [i+1, j+1]
        
    return [] 

numbers = [2,7,11,15]
target = 9

print(twoSum(numbers, target))

numbers = [2, 3, 4]
target = 6

print(twoSum(numbers, target))

numbers = [-1, 0]
target = -1

print(twoSum(numbers, target))