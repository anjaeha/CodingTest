from collections import deque

def bfs(g, graph, N, K):
    distance = [999999] * (N+1)
    distance[1] = 0
    q = deque([g])
    
    while q:
        temp = q.popleft()
        start = temp[0]
        cost = temp[1]

        for i in graph[start]:
            end, new_cost = i[0], i[1]
            
            if cost + new_cost <= K and cost + new_cost < distance[end]:
                distance[end] = cost + new_cost
                q.append([end, cost + new_cost])
                
    return distance

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N+1)]
    
    for i, j, k in road:
        graph[i].append([j, k])
        graph[j].append([i, k])
        
    lst = bfs([1, 0], graph, N, K)
    
    for i in lst:
        if i <= K:
            answer += 1
            
    return answer

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))