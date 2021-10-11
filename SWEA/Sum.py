T = 10

for tc in range(1, T + 1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]
    MAX = -1
    for i in range(100):
        MAX = max(MAX, sum(graph[i]))
    
    for i in range(100):
        temp = []
        for j in range(100):
            temp.append(graph[j][i])
        MAX = max(MAX, sum(temp))
    
    right = 0
    for i in range(100):
        right += graph[i][i]
    
    left = 0
    for i in range(100):
        left += graph[i][99 - i]

    print("#%d %d" %(tc, max(MAX, right, left)))