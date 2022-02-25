n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
arr = []
candi = []
visit = [False] * n

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
        visit[i] = False

dfs(0)
for i in list(set(candi)):
    print(*i)