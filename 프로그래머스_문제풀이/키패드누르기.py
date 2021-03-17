def solution(numbers, hand):
    lastL = 10
    lastR = 12
    answer = ''
    
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            lastL = i
        elif i in [3,6,9]:
            answer += 'R'
            lastR = i
        else:
            i = 11 if i == 0 else i
            
            absL = abs(i - lastL)
            absR = abs(i - lastR)
            
            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                answer += 'R'
                lastR = i
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                answer += 'L'
                lastL = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lastL = i
                else:
                    answer += 'R'
                    lastR = i
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))