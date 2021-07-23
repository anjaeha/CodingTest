import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = [i for i in range(1, n+1)]
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
