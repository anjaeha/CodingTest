from collections import deque
n = int(input())
s = list(map(int, input().split()))

graph = [[] for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(1, temp[0] + 1):
        graph[i].append(temp[j] - 1)

MIN = 10000
def dfs(cnt, end):
    global MIN
    if cnt == end:
        left, right = [], []
        for i in range(n):
            if visit[i]:
                left.append(i)
            else:
                right.append(i)
        ans1 = bfs(left)
        ans2 = bfs(right)
        if ans1 == 0 or ans2 == 0:
            return
        else:
            temp = abs(ans1 - ans2)
            if MIN > temp:
                MIN = temp
            return


    for i in range(n):
        if visit[i]:
            continue
        visit[i] = True
        dfs(cnt + 1, end)
        visit[i] = False

# 연결이 되어있는지 확인하고 인구수가 몇인지 구함
def bfs(array):
    q = deque()
    q.append(array[0])
    check = [False] * n
    check[array[0]] = True
    cnt = 1
    ans = 0
    while q:
        x = q.popleft()
        ans += s[x]
        for nx in graph[x]:
            if nx in array and check[nx] == False:
                check[nx] = True
                q.append(nx)
                cnt += 1
    
    if cnt == len(array):
        return ans
    else:
        return 0


for i in range(1, n // 2 + 1):
    visit = [False] * n
    dfs(0, i)

print(MIN if MIN != 10000 else - 1)