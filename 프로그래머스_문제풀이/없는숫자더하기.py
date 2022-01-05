def solution(numbers):
    answer = 0
    for i in range(10):
        if i in numbers:
            continue
        else:
            answer += i
    
    return answer