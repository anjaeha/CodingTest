import sys
input = sys.stdin.readline

n, m = map(int, input().split())
t = list(map(int, input().split()))

left = 1
right = max(t)

while left <= right:
    cnt = 0
    mid = (left + right) // 2

    for i in range(n):
        cnt += (t[i] - mid if t[i] - mid >= 0 else 0)
    
    if cnt >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)