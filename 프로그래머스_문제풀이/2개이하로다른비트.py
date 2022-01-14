def solution(numbers):
    answer = []
    
    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            temp = ['0'] + list(bin(number)[2:])
            for i in range(1, len(temp) + 1):
                if temp[-i] == '0':
                    temp[-i] = '1'
                    temp[-i + 1] = '0'
                    break
            answer.append(int(''.join(temp), 2))
    return answer