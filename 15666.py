n, m = map(int, input().split())

num = list(map(int, input().split()))
num.sort()
check = [False] * n

arr = []
answer = []

def dfs(cnt):
    if (cnt == m):
        answer.append(tuple(arr))
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

for i in sorted(list(set(answer))):
    print(*i)
