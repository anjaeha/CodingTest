import sys
from collections import Counter
input = sys.stdin.readline

n, k = map(int, input().split())
# 최소 antic 5개를배워야 할 수있음.
MAX = -sys.maxsize

words = [set(input().strip()) for _ in range(n)]

if k < 5 or k == 26:
    print(0 if k <= 5 else n)
    exit()

learn = [False] * 26

for i in ('a', 'c', 'i', 'n', 't'):
    learn[ord(i) - ord('a')] = True

def dfs(idx, cnt):
    global MAX

    if cnt == k - 5:
        temp = 0
        for word in words:
            for i in word:
                if learn[ord(i) - ord('a')] == False:
                    break
            else:
                temp += 1

        MAX = max(MAX, temp)
        return
    
    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False

dfs(0, 0)
print(MAX)