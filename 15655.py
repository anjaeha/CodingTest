n, m = map(int, input().split())

num = []
cheeck = [False] * n
arr = []

num.extend(map(int, input().split()))
num.sort()

def dfs(cnt):
    if (cnt == m):
        print(*arr)
        return
    
    for i in range(n):
        if (cheeck[i]):
            continue

        cheeck[i] = True
        arr.append(num[i])
        dfs(cnt+1)
        arr.pop()

        for j in range(i+1, n):
            cheeck[j] = False
        

dfs(0)