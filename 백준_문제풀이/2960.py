import sys
input = sys.stdin.readline

n, k = map(int, input().split())

s = [i for i in range(2, n+1)]

cnt = []

while s != []:
    temp = s[0]

    for i in s:
        if i % temp == 0:
            cnt.append(i)
            s.remove(i)

print(cnt[k - 1])