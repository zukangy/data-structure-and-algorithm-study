# 853. Car Fleet


def carFleet(target, position, speed):
    
    if not position:
        return 0
    
    if len(position) == 1:
        return 1
    
    pair = [[p, s] for p, s in zip(position, speed)]
    stack = []
    print(pair)
    print(sorted(pair))
    for p, s in sorted(pair)[::-1]:
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)
    


target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(carFleet(target, position, speed))