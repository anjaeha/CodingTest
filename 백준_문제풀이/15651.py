n, m = map(int, input().split())

arr = []
num = [i+1 for i in range(n)]
check = [False] * n

def dfs(cnt):
    if (cnt == m):
        print(*arr)
        return

    for i in range(n):
        check[i] = True
        arr.append(num[i])
        dfs(cnt+1)
        arr.pop()

        check[i] = False


dfs(0)