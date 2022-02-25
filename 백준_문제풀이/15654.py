n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
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