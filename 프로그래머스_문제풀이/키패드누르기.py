def solution(numbers, useHand):
    answer = ''
    hand = [10, 12]
    
    for i in range(len(numbers)):
        if numbers[i] == 0:
            numbers[i] = 11
    
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            hand[0] = number
        elif number in [3, 6, 9]:
            answer += 'R'
            hand[1] = number
        else:
            leftDis = abs(hand[0] - number) // 3 + abs(hand[0] - number) % 3
            rightDis = abs(hand[1] - number) // 3 + abs(hand[1] - number) % 3
            
            if leftDis < rightDis:
                answer += 'L'
                hand[0] = number
            elif leftDis > rightDis:
                answer += 'R'
                hand[1] = number
            elif leftDis == rightDis:
                if useHand == 'right':
                    answer += 'R'
                    hand[1] = number
                else:
                    answer += 'L'
                    hand[0] = number
    return answer