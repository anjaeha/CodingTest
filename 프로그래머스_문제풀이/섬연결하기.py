def solution(n, costs):
    costs.sort(key=lambda x: x[2])

    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]

    def union(parents, a, b):
        a = find(parent, a)
        b = find(parent, b)

        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i

    answer = 0
    for edge in costs:
        a, b, cost = edge

        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            answer += cost

    return answer