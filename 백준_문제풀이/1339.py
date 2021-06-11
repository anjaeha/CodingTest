import sys
input = sys.stdin.readline

n = int(input())
s = [list(input().strip()) for _ in range(n)]
result = 0
cnt = 9

a = [0 for _ in range(26)]

for i in s:
    li = len(i)
    for j in range(li):
        a[ord(i[j]) - 65] += 10 ** (li - j - 1)
a.sort(reverse=True)

for i in a:
    result += i * cnt
    cnt -= 1

print(result)