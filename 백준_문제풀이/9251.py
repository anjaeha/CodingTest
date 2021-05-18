import sys
input = sys.stdin.readline

s1 = list(input().strip())
s2 = list(input().strip())

s1_len = len(s1)
s2_len = len(s2)

dp = [[0] * (s2_len + 1) for i in range(s1_len + 1)]
s = []
for i in range(s1_len):
    for j in range(s2_len):
        if s1[i] == s2[j]:
            dp[i+1][j+1] = dp[i][j] + 1

        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

print(dp[s1_len][s2_len])
