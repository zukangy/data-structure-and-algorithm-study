# 20. Valid parenthesis
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 
# s consists of parentheses only '()[]{}'

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false


# Use the stack approach to check whether each sub-expression is valid. 
# There are two solutions, where isValid is my solution which looks less readable but a lot faster as it terminates when it sees a 
# unmatching pattern, while isValidStandardSolution is provided by leetcode where it checks through the entire array and makes 
# final judgement after the traversal. 
def isValid(s: str) -> bool:
        if len(s) % 2 == 1:
            print('a')
            return False 

        matching_patterns = {"}": "{", ")": "(", "]": "["}

        stack = []
        for i in s:
            if i in matching_patterns:
                if stack:
                    if stack[-1] != matching_patterns[i]:
                        return False 
                    else:
                        stack.pop()
                else:
                    return False 
            else:
                stack.append(i)
        return not stack  
    
    
def isValidStandardSolution(s: str) -> bool:
        if len(s) % 2 == 1:
            print('a')
            return False 

        matching_patterns = {"}": "{", ")": "(", "]": "["}

        stack = []
        for i in s:
            if i in matching_patterns:
                top_element = stack.pop() if stack else "#"
                if matching_patterns[i] != top_element:
                    return False 
            else:
                stack.append(i)
        return not stack  
    
    
s = "()"
print(isValid(s))

s = "()[]{}"
print(isValid(s))

s = "{[]}"
print(isValid(s))