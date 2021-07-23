import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = [i for i in range(1, n+1)]
used = [False] * n
arr = []

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