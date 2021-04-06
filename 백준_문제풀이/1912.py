n = int(input())
s = list(map(int, input().split()))

dp = [-1001 for _ in range(n)]
dp[0] = s[0]

for i in range(1, n):
    if dp[i-1] +s[i] < s[i]:
        dp[i] = s[i]
    else:
        dp[i] = max(dp[i-1] + s[i], s[i])
    
print(max(dp))



"""
n = int(input())
s = list(map(int, input().split()))

sum = [s[0]]
for i in range(n - 1):
    sum.append(max(sum[i] + s[i+1], s[i+1]))

print(max(sum))
"""