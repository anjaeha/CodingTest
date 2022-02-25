n, m = map(int, input().split())

visit = [False] * n
numbers = [i for i in range(1, n + 1)]
arr = []

def dfs(cnt):
    if cnt == m:
        print(*arr)
        return

    for i in range(n):
        if visit[i]:
            continue
        visit[i] = True

        arr.append(numbers[i])
        dfs(cnt + 1)
        arr.pop()
        for j in range(i + 1, n):
            visit[j] = False

dfs(0)