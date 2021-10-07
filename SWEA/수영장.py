# 1일이용권, 1달이용권, 3달이용권, 1년 이용권
# 가장 적은 비용으로 수영장을 이용할 수 있는 가격 찾기

T = int(input())

for case in range(1, T + 1):
    day, month, month3, year = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    dp = [0] * 13

    for i in range(1, 13):
        dp[i] = min(plan[i] * day, month) + dp[i - 1]

        if i > 2:
            dp[i] = min(dp[i], dp[i - 3] + month3)
    
    result = min(dp[12], year)
    print("#%d %d" %(case, result))