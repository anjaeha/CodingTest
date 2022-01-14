def solution(number, k):
    stack = [number[0]]
    
    for num in number[1:]:
        while stack and stack[-1] < num and k:
            k -= 1
            stack.pop()
        stack.append(num)
    
    if k:
        stack = stack[:-k]
        
    return ''.join(stack)