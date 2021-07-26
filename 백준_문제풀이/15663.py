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


"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
arr = []
answer = []
used = [False] * n

def dfs(depth):
    if depth == m:
        print(*arr)
        return

    temp = 0
    for i in range(n):
        if used[i] or temp == num[i]:
            continue

        used[i] = True
        temp = num[i]
        arr.append(num[i])
        dfs(depth + 1)
        arr.pop()

        used[i] = False


dfs(0)
중복을 확인하는 변수 temp 선언.
"""