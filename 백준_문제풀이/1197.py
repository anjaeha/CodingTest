import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
graph.sort(key = lambda x : x[2])


cost = 0

p = [i for i in range(n+1)]

def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]

def union(u, v):
    root1 = find(u)
    root2 = find(v)
    p[root2] = root1

for e in graph:
    a, b, c = e

    if find(a) != find(b):
        union(a, b)
        cost += c

print(cost)