def solution(s):
    zero = 0 # 제거할 0의 개수
    count = 0 # 회차
    
    while s != '1':
        temp = s.count('0')
        zero += temp
        s = str(bin(len(s) - temp)[2:])
        count += 1

    return [count, zero]