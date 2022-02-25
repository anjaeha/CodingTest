n, m = map(int, input().split())
numbers = sorted(set(list(map(int, input().split()))))
visit = [False] * len(numbers)
arr = []

def dfs(cnt):
    if cnt == m:
        print(*arr)
        return

    for i in range(len(numbers)):
        if visit[i]:
            continue

        arr.append(numbers[i])
        dfs(cnt + 1)
        visit[i] = True
        arr.pop()
        for j in range(i + 1, len(numbers)):
            visit[j] = False

dfs(0)