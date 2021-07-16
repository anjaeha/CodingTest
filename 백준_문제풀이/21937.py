import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
n, m = map(int, input().split())
s = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    s[b].append(a)
visit = [0] * (n+1)
target = int(input())

answer = set()

def dfs(x):
    if visit[x] == 1:
        return
    for i in range(len(s[x])):
        dfs(s[x][i])
    answer.add(x)
    visit[x] = 1


for i in s[target]:
    dfs(i)

print(len(answer))