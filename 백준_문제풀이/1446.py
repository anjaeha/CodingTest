import sys
input = sys.stdin.readline

n, d = map(int, input().split())
visit = [i for i in range(d+1)]
s = [[] for _ in range(10001)]

for _ in range(n):
    x, y, r = map(int, input().split())
    s[x].append((y, r))

for i in range(d+1):
    if i != 0:
        visit[i] = min(visit[i], visit[i-1] + 1)
    
    for end, wei in s[i]:
        if end  <= d and visit[end] > visit[i] + wei:
            visit[end] = visit[i] + wei

print(visit[d])