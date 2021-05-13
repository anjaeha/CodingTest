def solution(s):
    answer = 0
    start = ['(', '[', '{']
    end = [')', ']', '}']

    for i in range(len(s)):
        s = s[1:] + s[0]

        stack = []

        for x in s:
            if x in end and len(stack) > 0:
                for i in range(3):
                    if stack[-1] == start[i] and x == end[i]:
                        stack.pop()
                        break

            else:
                stack.append(x)

        if not stack:
            answer += 1

    return answer

print(solution("[](){}"))