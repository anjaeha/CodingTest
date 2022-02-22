t = int(input())

for tc in range(t):
    n = int(input())
    coin = list(map(int, input().split()))
    money = int(input())

    dp = [0] * (money + 1)
    dp[0] = 1

    for i in coin:
        for j in range(1, money + 1):
            if j - i >= 0:
                dp[j] += dp[j - i]
    print(dp[money])