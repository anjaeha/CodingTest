import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
d = int(input())
s = [[0] * n for _ in range(n)]
visit = [0] * n
cnt = 0
def dfs(root):
    global cnt
    visit[root] = 1
    flag = False

    for i in range(n):
        if visit[i] == 0 and s[i][root] == 1:
            visit[i] = 1
            flag = True
            dfs(i)

    if not flag:
        cnt += 1


for i in range(n):
    if li[i] == -1:
        root = i
    else:
        s[i][li[i]] = 1
        s[li[i]][i] = 1

for i in range(n):
    s[i][d] = 0
    s[d][i] = 0

dfs(root)

if root == d:
    print(0)
else:
    print(cnt)