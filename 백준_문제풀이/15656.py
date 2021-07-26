import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
arr = []

def dfs(depth):
    if depth == m:
        print(*arr)
        return
    
    for i in range(n):
        arr.append(num[i])
        dfs(depth + 1)
        arr.pop()
dfs(0)