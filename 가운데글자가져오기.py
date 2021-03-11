def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        answer = answer + s[len(s) // 2 - 1] + s[len(s) // 2]
    else:
        answer = answer + s[len(s) // 2]
    return answer