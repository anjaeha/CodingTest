from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
c, h = [], []

for i in range(n):
    for j in range(n):
        if s[i][j] == 1:
            h.append((i, j))
        elif s[i][j] == 2:
            c.append((i, j))

c = combinations(c, m)

result = 1000000000
for k in c:
    min_result = 0
    for i, j in h:
        min_num = 10000000000
        for x, y in k:
            min_num = min(min_num, abs(x - i) + abs(y - j))
        min_result += min_num
    result = min(result, min_result)

print(result)