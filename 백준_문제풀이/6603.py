from itertools import combinations

while 1:
    k = list(map(int, input().split()))
    if k[0] == 0:
        break

    del k[0]

    answer = list(combinations(k, 6))
    
    for i in answer:
        for j in i:
            print(j, end = ' ')
        print()
    print()

"""
import sys
input = sys.stdin.readline

def dfs(cnt):
    if cnt == 6:
        print(*answer)
        return

    for i in range(n):
        if visit[i]:
            continue

        visit[i] = True
        answer.append(s[i])
        dfs(cnt + 1)
        answer.pop()
        for j in range(i + 1, n):
            visit[j] = False

while 1:
    s = list(map(int, input().split()))
    n = s[0]
    if n == 0:
        break
    s = s[1:]
    answer = []
    visit = [False] * n
    dfs(0)

    print()
"""