n, m = map(int, input().split())

check = [False] * n
num = list(map(int, input().split()))
num.sort()
arr = []
answer = []

def bfs(cnt):
    if (cnt == m):
        answer.append(tuple(arr))
        return

    for i in range(n):
        if(check[i]):
            continue

        check[i] = True
        arr.append(num[i])
        bfs(cnt+1)
        arr.pop()

        check[i] = False

bfs(0)

for x in sorted(list(set(answer))):
    print(*x)