def solution(numbers):
    answer = []
    for i in range(0, len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    
    answer = list(set(answer))
    answer.sort()

    return answer

    # return sorted(list(set(answer)))한줄로 정리가능
    
print(solution([5,0,2,7]))