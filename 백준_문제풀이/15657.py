import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
arr = []
used = [False] * n

def dfs(depth):
    if depth == m:
        print(*arr)
        return

    for i in range(n):
        if used[i]:
            continue

        
        arr.append(num[i])
        dfs(depth + 1)
        used[i] = True
        arr.pop()

        for j in range(i + 1, n):
            used[j] = False

dfs(0)