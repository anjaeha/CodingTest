n, k = map(int, input().split())
s = list(map(int, input().split()))
m = [0 for i in range(n)]
cnt = 0

for i in range(k):
    isTrue = False
    for j in range(n):
        if m[j] == s[i] or m[j] == 0:
            isTrue = True
            m[j] = s[i]
            break
    
    if isTrue:
        continue
    else:
        a = 0
        for j in range(n):
        



# https://pacific-ocean.tistory.com/357
# https://www.acmicpc.net/problem/1700