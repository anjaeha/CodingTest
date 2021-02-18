n, m = map(int, input().split())

num = [i+1 for i in range(n)]
check = [False] * n
arr = []

def dfs(cnt):
    if (cnt == m):
        print(*arr)
        return
    
    for i in range(n):
        if (check[i]):
            continue

        check[i] = True
        arr.append(num[i])
        dfs(cnt+1)

        arr.pop()

        check[i] = False
        
dfs(0)


