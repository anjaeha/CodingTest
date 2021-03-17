T = int(input())


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]

        for i in range(4):
            q = a + dx[i]
            w = b + dy[i]

            if 0 <= q < N and 0 <= w < M and s[q][w] == 1:
                s[q][w] = 0
                queue.append([q,w])




for i in range(T):
    M, N , K = map(int, input().split())

    s = [[0] * M for i in range(N)]
    cnt = 0
    
    for j in range(K):
        a, b = map(int, input().split())
        s[b][a] = 1

    for q in range(N):
        for w in range(M):
            if s[q][w] == 1:
                bfs(q, w)
                s[q][w] = 0
                cnt += 1

    print(cnt)


    # bfs 이해 필요함
    # dfs 한 30프로 이해한듯?