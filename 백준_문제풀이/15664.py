n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
visit = [False] * n
arr = []
candi = []

def dfs(cnt):
    if cnt == m:
        candi.append(tuple(arr))
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
candi = sorted(list(set(candi)))
for i in candi:
    print(*i)