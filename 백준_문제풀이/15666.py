import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(sorted(map(int, input().split())))
used = [False] * n
arr = []
answer = []

def dfs(depth):
    if depth == m:
        answer.append(tuple(arr))
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

for x in sorted(set(answer)):
    print(*x)