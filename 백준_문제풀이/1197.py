
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(e)]

edges.sort(key = lambda x : x[2])

parent = [i for i in range(v + 1)]

result = 0
for edge in edges:
    a, b, cost = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(result)