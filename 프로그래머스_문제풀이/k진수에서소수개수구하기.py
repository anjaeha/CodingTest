def prime_number(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    calc = ''
    while n > 0:
        calc += str(n % k)
        n //= k
    calc = calc[::-1]
    
    answer = 0
    
    temp = calc.split('0')
    for i in temp:
        if i:
            if prime_number(int(i)):
                answer += 1

    return answer