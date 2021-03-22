import sys
input = sys.stdin.readline
from heapq import heappush, heappop

inf = 10000000
v, e = map(int, input().split())
start = int(input())
s = [[] for _ in range(v+1)]

visit = [inf] * (v+1)

for _ in range(e):
    a, b, c = map(int, input().split())
    s[a].append([b, c])

q = []
def dij(start):
    visit[start] = 0
    heappush(q, [0, start])
    
    while q:
        w, n = heappop(q)
        for n_n, wei in s[n]:
            n_w = wei + w
            if n_w < visit[n_n]:
                visit[n_n] = n_w
                heappush(q, [n_w, n_n])

dij(start)

for i in range(1, v+1):
    if visit[i] != inf:
        print(visit[i])
    else:
        print('INF')