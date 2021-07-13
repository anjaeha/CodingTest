import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    s[x].append(y)
    s[y].append(x)

answer = set(s[1])

for i in s[1]:
    answer.update(s[i])

print(len(answer) - 1 if len(answer) != 0 else 0)