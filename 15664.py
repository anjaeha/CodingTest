n, m = map(int, input().split())


num = list(map(int, input().split()))
num.sort()
check = [False] * n
arr = []
answer = []

def dfs(cnt):
    if(cnt == m):
        print(*arr)
        return
    
    for i in range(n):
        if(check[i]):
            continue
        check[i] = True
        arr.append(num[i])
        
        dfs(cnt+1)
        arr.pop()

dfs(0)

