# 150. Evaluate Reverse Polish Notation

# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.

def evalRPN(tokens: list[str]) -> int:
        stack = []

        operators = {
            '+': lambda a, b: a + b,
             '-': lambda a, b: a - b,
             '*': lambda a, b: a * b,
             '/': lambda a, b: int(a / b),
        }

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                 right_num = stack.pop()
                 left_num = stack.pop()

                 result = operators[t](left_num, right_num)
                 stack.append(result)
        
        return stack.pop() 
    
    
tokens = ["2","1","+","3","*"]
print(evalRPN(tokens))

tokens = ["4","13","5","/","+"]
print(evalRPN(tokens))

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))