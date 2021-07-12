import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]

c = []
h = []
for i in range(n):
    for j in range(n):
        if s[i][j] == 1:
            h.append((i, j))
        elif s[i][j] == 2:
            c.append((i, j))

c = list(combinations(c, m))

result = 10000000001
for i in c:
    min_result = 0
    for h_x, h_y in h:
        temp = 10000000001
        for c_x, c_y in i:
            temp = min(temp, abs(h_x - c_x) + abs(h_y - c_y))
        min_result += temp
    result = min(result, min_result)

print(result)