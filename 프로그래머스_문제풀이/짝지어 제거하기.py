def solution(s):
    stack = []
    if len(s) % 2 == 1:
        return 0

    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    if stack == []:
        return 1
    else:
        return 0
    

print(solution("baabaa"))