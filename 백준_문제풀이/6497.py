import sys
input = sys.stdin.readline


while 1:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(m)]
    graph.sort(key = lambda x : x[2])
    cost = 0 

    p = [i for i in range(n+1)]
    total = 0
    for i in range(m):
        total += graph[i][2]

    def find(u):
        if u != p[u]:
            p[u] = find(p[u])
        return p[u]

    def union(u, v):
        root1 = find(u)
        root2 = find(v)
        p[root2] = root1

    for edge in graph:
        u, v, wt = edge

        if find(u) != find(v):
            union(u, v)
            cost += wt

    print(total - cost)
