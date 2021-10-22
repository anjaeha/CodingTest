def make_candi(depth):
    if depth == n // 2:
        candi.append(list(temp))
        return

    for i in range(n):
        if visit[i]:
            continue
        visit[i] = True
        temp.append(i)
        make_candi(depth + 1)
        temp.pop()
        for j in range(i + 1, n):
            visit[j] = False

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    result = 987654321

    length = n // 2
    temp = []
    candi = []
    visit = [False] * n
    make_candi(0)

    for i in range(len(candi)):
        cur = candi[i]
        other = []
        for num in range(n):
            if num not in cur:
                other.append(num)

        size1 = 0
        size2 = 0
        for a in range(len(cur)):
            for b in range(a + 1, len(cur)):
                x = cur[a]
                y = cur[b]
                size1 += graph[x][y]
                size1 += graph[y][x]
        for a in range(len(other)):
            for b in range(a + 1, len(other)):
                x = other[a]
                y = other[b]
                size2 += graph[x][y]
                size2 += graph[y][x]

        result = min(result, abs(size1 - size2))

    print("#%d %d" %(tc, result))