n, m = map(int, input().split())
check = [False] * n
num = list(map(int, input().split()))
num.sort()

answer = []
arr = []

def dfs(cnt):
    if (cnt == m):
        answer.append(tuple(arr))
        return

    for i in range(n):


        check[i] = True
        arr.append(num[i])
        dfs(cnt+1)
        arr.pop()


        check[i] = False

dfs(0)

for i in sorted(list(set(answer))):
    print(*i)