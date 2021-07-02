def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    
    for number in numbers:
        if number in [1,4,7]:
            answer += 'L'
            left = number
        elif number in [3,6,9]:
            answer += 'R'
            right = number
        else:
            if number == 0:
                number = 11
            Aleft = abs(left - number)
            Aright = abs(right - number)
            
            if sum(divmod(Aleft, 3)) > sum(divmod(Aright, 3)):
                answer += 'R'
            elif sum(divmod(Aleft, 3)) < sum(divmod(Aright, 3)):
                answer += 'L'
            else:
                if hand == 'left':
                    answer += 'L'
                else:
                    answer += 'R'
            if answer[-1] == 'R':
                right = number
            else:
                left = number

    return answer