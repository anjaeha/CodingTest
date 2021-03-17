n, m = map(int, input().split())

arr = []
check = [False] * n
num = []

num.extend(map(int, input().split()))

num.sort()

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