T = int(input())

for case in range(T):
    K = int(input())  # 층
    N = int(input())  # 호
    
    graph = [i for i in range(1, N+1)] # 1층 집 세팅

    for l in range(K):
        for m in range(1, N):
            graph[m] += graph[m-1]

    print(graph[N-1])
