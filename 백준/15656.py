n, m = map(int, input().split())

arr = []
num = []
num.extend(map(int, input().split()))
num.sort()

check = [False] * n

def bfs(cnt):
    if (cnt == m):
        print(*arr)
        return

    for i in range(n):


        check[i] = True
        arr.append(num[i])
        bfs(cnt+1)
        arr.pop()

        check[i] = False


bfs(0)