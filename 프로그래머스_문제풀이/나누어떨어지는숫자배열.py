def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    
    answer.sort()
    return answer if answer else [-1]