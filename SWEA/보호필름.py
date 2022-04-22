def check():
    for y in range(m):
        MAX = 0
        for x in range(n):
            cnt = 1
            for r in range(x + 1, n):
                if graph[x][y] == graph[r][y]:
                    cnt += 1
                else:
                    break
            MAX = max(MAX, cnt)
        if MAX < k:
            return False
    return True

def make_candi(depth, count):
    if depth == count:
        candi.append(list(temp))
        return

    for i in range(n):
        if visit[i]:
            continue
        visit[i] = True
        temp.append(i)
        make_candi(depth + 1, count)
        temp.pop()
        for j in range(i + 1, n):
            visit[j] = False

T = int(input())

for tc in range(T):
    n, m, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    candi = []
    for idx in range(n + 1):
        visit = [False] * n
        temp = []
        make_candi(0, idx)
    result = 987654321
    flag = False
    board = [i[:] for i in graph]

    for idx in range(len(candi)):
        graph = [i[:] for i in board]
        cur = candi[idx]
        for c in range(len(cur)):
            for i in range(m):
                graph[cur[c]][i] = 0
        if check():
            flag = True
            result = len(cur)
            break

        for c in range(len(cur)):
            for i in range(m):
                graph[cur[c]][i] = 1
        if check():
            flag = True
            result = len(cur)
            break

        for c in range(len(cur) // 2):
            for i in range(m):
                graph[cur[c]][i] = 0
        for c in range(len(cur) // 2, len(cur)):
            for i in range(m):
                graph[cur[c]][i] = 1

        if check():
            flag = True
            result = len(cur)
            break

        for c in range(len(cur) // 2):
            for i in range(m):
                graph[cur[c]][i] = 1
        for c in range(len(cur) // 2, len(cur)):
            for i in range(m):
                graph[cur[c]][i] = 0
        if check():
            flag = True
            result = len(cur)
            break

    print("#%d %d" %(tc + 1, result))