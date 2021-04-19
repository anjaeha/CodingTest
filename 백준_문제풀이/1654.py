import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = []
for i in range(k):
    arr.append(int(input()))

left = 1
right = max(arr)

while left <= right:
    sum = 0
    mid = (left + right) // 2

    for i in arr:
        sum += i // mid

    if sum >= n:
        left = mid + 1
    else:
        right = mid - 1

print(right)