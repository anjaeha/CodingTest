def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            dfs(n, computers, com, visited)
            answer += 1    
    return answer

def dfs(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if computers[com][connect] == 1:
            if visited[connect] == False:
                dfs(n, computers, connect, visited)


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))