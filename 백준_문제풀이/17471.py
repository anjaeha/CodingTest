from collections import deque

def bfs(array):
    q = deque()
    q.append(array[0])
    check = [False] * n
    check[array[0]] = True
    cnt, ans = 1, 0

    while q:
        x = q.popleft()
        ans += people[x]
        for nx in link[x]:
            if nx in array and not check[nx]:
                check[nx] = True
                cnt += 1
                q.append(nx)

    if cnt == len(array):
        return ans
    else:
        return 0

def dfs(cnt, x, end):
    global MIN
    if cnt == end:
        left, right = deque(), deque()
        for i in range(n):
            if c[i]:
                left.append(i)
            else:
                right.append(i)
        ans1 = bfs(left)
        ans2 = bfs(right)

        if ans1 == 0 or ans2 == 0:
            return
        MIN = min(MIN, abs(ans1 - ans2))
        return
    
    for i in range(x, n):
        if c[i]:
            continue
        c[i] = True
        dfs(cnt + 1, i, end)
        c[i] = False

n = int(input())
people = list(map(int, input().split()))
link = [[] for _ in range(n)]

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(1, temp[0] + 1):
        link[i].append(temp[j] - 1)

MIN = 1001
for i in range(1, n // 2 + 1):
    c = [False] * n
    dfs(0, 0, i)


print(MIN if MIN != 1001 else -1)