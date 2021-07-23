import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
used = [False] * n
arr = []

def dfs(depth):
    if depth == m:
        print(*arr)
        return

    for i in range(n):
        if used[i]:
            continue

        used[i] = True
        arr.append(num[i])
        dfs(depth + 1)
        arr.pop()

        for j in range(i + 1, n):
            used[j] = False

dfs(0)