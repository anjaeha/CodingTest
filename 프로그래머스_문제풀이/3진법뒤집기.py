def solution(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
        
    return int(s, 3)
    