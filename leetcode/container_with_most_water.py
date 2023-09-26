# 11. Container with most water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Create two pointers with each at one end of the list. At each iteration, move the pointer with the shorter height 1 position towards the other pointer
# The reasoning behind this solution is we always want to move the pointer with shorter height to the next to hopefully obtain a larger height to increase 
# the capacity
def maxArea(height: list[int]) -> int:
        current_v = 0
        max_v = 0
        i = 0
        j = len(height) - 1
        
        while i < j:
            current_v = (j - i) * min([height[i], height[j]])
            if current_v > max_v:
                max_v = current_v
            
            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1
        
        return max_v
    
    
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))

height = [1,1]
print(maxArea(height))