T = int(input())

for case in range(T):
    answer = 0
    num = input().split()
    N = float(num[0])
    for i in num:
        if i == '@':
            N = N * 3
        elif i == '%':
            N = N + 5
        elif i == '#':
            N = N - 7
    
    print("%.2f" % N)