from collections import deque

def count(start, visit, graph):
    q = deque([start])
    count = 1
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visit[i]:
                q.append(i)
                count += 1
                visit[i] = True
    return count

def solution(n, wires):
    answer = 1001
    graph = [[] for _ in range(n + 1)]
    
    for x, y in wires:
        graph[x].append(y)
        graph[y].append(x)
        
    for x, y in wires:
        visit = [False] * (n + 1)
        visit[x] = True
        visit[y] = True
        
        left = count(x, visit, graph)
        right = n - left
        answer = min(answer, abs(left - right))
        
    return answer