import sys, math
input = sys.stdin.readline

n = int(input())
location = [list(map(float, input().split())) for _ in range(n)]
cost = 0
p = [i for i in range(n+1)]

def find(u):
    if p[u] != u:
        p[u] = find(p[u])
    return p[u]

def union(u, v):
    root1 = find(u)
    root2 = find(v)
    p[root2] = root1

graph = []
for i in range(n - 1):
    for j in range(i + 1, n):
        graph.append((math.sqrt((location[i][0] - location[j][0])**2 + (location[i][1] - location[j][1])**2), i, j))

graph.sort()

for edge in graph:
    wt, x, y = edge

    if find(x) != find(y):
        union(x, y)
        cost += wt

print(round(cost, 2))