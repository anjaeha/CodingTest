import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = n - m
answer = 1

while n > k:
    answer *= n
    n -= 1

while m > 1:
    answer = answer // m
    m -= 1

print(answer)