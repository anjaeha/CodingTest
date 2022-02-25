n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
arr = []
visit = [False] * n

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