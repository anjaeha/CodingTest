n, m = map(int, input().split())


num = list(map(int, input().split()))
num.sort()
check = [False] * n
arr = []
answer = []

def dfs(cnt):
    if(cnt == m):
        answer.append((tuple(arr)))
        return
    
    for i in range(n):
        if(check[i]):
            continue

        check[i] = True
        arr.append(num[i])
        
        dfs(cnt+1)
        arr.pop()

        for j in range(i+1, n):
            check[j] = False


dfs(0)

for x in sorted(list(set(answer))):
    print(*x)