import sys
input = sys.stdin.readline

n = int(input())
s = [[] for _ in range(n+1)]
visit = [0] * (n+1)

for _ in range(n-1):
    x, y = map(int, input().split())
    s[x].append(y)
    s[y].append(x)

q = [1]
result = {}

while q:
    now = q.pop()
    for i in s[now]:
        if visit[i] == 0:
            visit[i] = 1
            result[i] = now
            q.append(i)


for i in range(2, n+1):
    print(result[i])