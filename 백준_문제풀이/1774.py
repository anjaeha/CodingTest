import sys
input = sys.stdin.readline

n, m = map(int, input().split())
location = [list(map(int, input().split())) for _ in range(n)]
link = [list(map(int, input().split())) for _ in range(m)]
graph = []
cost = 0

for i in range(n-1):
    for j in range(i + 1, n):
        temp = ((location[i][0] - location[j][0]) ** 2 + (location[i][1] - location[j][1]) ** 2) ** 0.5
        graph.append((i + 1, j + 1, temp))

graph.sort(key = lambda x : x[2])
p = [i for i in range(n+1)]

def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]

def union(u, v):
    root1 = find(u)
    root2 = find(v)
    p[root2] = root1
for i in range(m):
    union(link[i][0], link[i][1])


for edge in graph:
    u, v, wt = edge

    if find(u) != find(v):
        union(u, v)
        cost += wt

print('%0.2f' %cost) 