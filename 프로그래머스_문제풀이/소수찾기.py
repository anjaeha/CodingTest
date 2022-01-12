from itertools import permutations

def prime_number(num):
    if num in [0, 1]:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = []
    numbers = list(numbers)    
    
    check = []
    for i in range(1, len(numbers) + 1):
        temp = list(permutations(numbers, i))
        check += temp
        
    for i in check:
        temp = int(''.join(i))
        
        if prime_number(temp):
            answer.append(temp)
            
    return len(set(answer))