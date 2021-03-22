import sys
input = sys.stdin.readline

t = int(input())
for case in range(t):
    n = int(input())
    MAX_N = n
    MIN_N = n
    MAX = ''
    m = [0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22]
    while MAX_N != 0:
        if MAX_N % 2 == 0:
            MAX += '1'
            MAX_N -= 2
        else:
            MAX += '7'
            MAX_N -= 3
    
    
    if n < 11:
        MIN = [m[n]]
    else:
        MIN = [8 for _ in range((n + 6) // 7)]
        if n % 7 == 1:
            MIN[0] = 1
            MIN[1] = 0
        elif n % 7 == 2:
            MIN[0] = 1
        elif n % 7 == 3:
            MIN[0] = 2
            MIN[1] = 0
            MIN[2] = 0
        elif n % 7 == 4:
            MIN[0] = 2
            MIN[1] = 0
        elif n % 7 == 5:
            MIN[0] = 2
        elif n % 7 == 6:
            MIN[0] = 6

    print(*MIN, sep = '', end = ' ')
    print(MAX)