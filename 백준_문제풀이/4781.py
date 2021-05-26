import sys
input = sys.stdin.readline


while 1:
    n, m = map(float, input().split())
    n = int(n)
    m = int(m * 100 + 0.5)

    if n == 0 and m == 0:
        break

    dp = [0] * (m+1)

    for case in range(n):
        c, p = map(float, input().split())
        c = int(c)
        p = int(p * 100 + 0.5)

        for i in range(p, m+1):
            dp[i] = max(dp[i], dp[i-p] + c)

    
    print(dp[m])