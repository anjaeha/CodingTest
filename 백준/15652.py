n, m = map(int, input().split())

num = [i+1 for i in range(n)]
check = [False] * n
arr = []

def dfs(cnt):
    if (cnt == m):
        print(*arr)
        return

    for i in range(n):
        if(check[i]):
            continue

        
        arr.append(num[i])
        dfs(cnt+1)
        check[i] = True
        arr.pop()

        for j in range(i+1, n):
            check[j] = False

dfs(0)