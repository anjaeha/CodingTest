def check(s):
    left, right = 0, 0
    flag = True
    stack = []

    for i in range(len(s)):
        if s[i] == '(':
            left += 1
            stack.append('(')
        else:
            right += 1
            if stack:
                stack.pop()
            else:
                flag = False
        if left == right:
            return i + 1, flag


def solution(p):
    if p == '':
        return ''

    idx, flag = check(p)
    u, v = p[:idx], p[idx:]

    if flag:
        return u + solution(v)

    answer = '(' + solution(v) + ')'
    for i in range(1, len(u) - 1):
        if u[i] == '(':
            answer += ')'
        else:
            answer += '('

    return answer