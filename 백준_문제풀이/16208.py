import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))

cnt = 0
len_s = len(s)
sum_s = sum(s)

for i in range(n):
    cnt += s[i] * (sum_s - s[i])
    sum_s -= s[i]

print(cnt)