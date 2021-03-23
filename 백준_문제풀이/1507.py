import sys
input = sys.stdin.readline

n = int(input())

s = []
s_ = [[1] * n for i in range(n)]

result = 0

for i in range(n):
    s.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j or j == k or i == k:
                continue   
            if s[i][j] == s[k][i] + s[k][j]:
                s_[i][j] = 0
            elif s[i][j] > s[k][i] + s[k][j]:
                result = -1


if result != -1:
    for i in range(n):
        for j in range(i, n):
            if s_[i][j]:
                result += s[i][j]

print(result)