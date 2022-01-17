def solution(n):
    graph = [[0] * i for i in range(1, n + 1)]

    cnt = 1
    x, y = -1, 0
    
    for i in range(n):
        for j in range(n - i):
            
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x, y = x - 1, y - 1
                
            graph[x][y] = cnt
            cnt += 1
    
    result = []
    for i in range(n):
        for j in range(len(graph[i])):
            result.append(graph[i][j])
            
    return result