import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
graph.sort(key = lambda x : x[2])
total = 0
for i in range(m):
    total += graph[i][2]

p = [0]

for i in range(1, n+1):
    p.append(i)

def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]

def union(u, v):
    root1 = find(u)
    root2 = find(v)
    p[root2] = root1

tree_edges = 0
mst_cost = 0

while 1:
    if tree_edges == n - 1:
        break
    u, v, wt = graph.pop(0)
    if find(u) != find(v):
        union(u, v)
        mst_cost += wt
        tree_edges += 1

print(total - mst_cost)

# 시간초과 나옴.
# MST 문제 풀어보기!