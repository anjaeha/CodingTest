import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

left = 0
right = house[-1]

while left <= right:
    mid = (left + right) // 2
    gap = house[0]
    cnt = 1

    for i in range(1, n):
        if house[i] >= mid + gap:
            gap = house[i]
            cnt += 1

    if cnt >= c:
        left = mid + 1
        result = mid
    else:
        right = mid - 1

print(result)