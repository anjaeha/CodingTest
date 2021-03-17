n, m = map(int, input().split())

num = []
arr = []
check = [False] * n
num.extend(map(int, input().split()))
num.sort()


def bfs(cnt):
    if (cnt == m):
        print(*arr)
        return

    for i in range(n):
        
        if (check[i]):
            continue
        
        arr.append(num[i])
        
        bfs(cnt+1)
        check[i] = True
        arr.pop()

        for j in range(i+1, n):
            check[j] = False

bfs(0)