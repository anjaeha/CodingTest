n, m = map(int, input().split())

numbers = [i for i in range(1, n + 1)]
visit = [False] * n
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
        visit[i] = False

dfs(0)