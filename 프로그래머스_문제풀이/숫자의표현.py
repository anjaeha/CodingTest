def solution(n):
    left, right = 0, 0
    result = 0
    answer = 1
    
    for i in range(n + 1):
        if result < n:
            right += 1
            result += right
        elif result > n:
            left += 1
            result -= left
        else:
            answer += 1
            right += 1
            result += right
    
    return answer