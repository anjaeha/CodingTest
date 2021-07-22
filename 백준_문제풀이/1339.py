import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(str, input().strip())) for _ in range(n)]
a = [0 for i in range(26)]

cnt = 9
for k in arr:
    idx = len(k)
    for i in range(len(k)):
        a[ord(k[i]) - 65] += 10 ** (idx - i - 1)
    
a.sort(reverse=True)

answer = 0
for i in a:
    answer += cnt * i
    cnt -= 1

print(answer)