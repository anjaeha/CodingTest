import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dp1 = [[0] * m for _ in range(n)]
dp2 = [[0] * m for _ in range(n)]

for i in range(n-1, -1, -1):
    for j in range(m):
        if i == n - 1 and j == 0:
            dp1[i][j] = graph[i][j]
        elif j == 0:
            dp1[i][j] = dp1[i+1][j] + graph[i][j]
        elif i == n - 1:
            dp1[i][j] = dp1[i][j-1] + graph[i][j]
        else:
            dp1[i][j] = max(dp1[i][j-1], dp1[i+1][j]) + graph[i][j]

for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        if i == n - 1 and j == m - 1:
            dp2[i][j] = graph[i][j]
        elif i == n - 1:
            dp2[i][j] = dp2[i][j+1] + graph[i][j]
        elif j == m - 1:
            dp2[i][j] = dp2[i+1][j] + graph[i][j]
        else:
            dp2[i][j] = max(dp2[i+1][j], dp2[i][j+1]) + graph[i][j]

MAX = -987654321
for i in range(n):
    for j in range(m):
        MAX = max(MAX, dp1[i][j] + dp2[i][j])

print(MAX)