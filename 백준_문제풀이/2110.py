import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

left = 1
right = house[-1] - house[0]

while left <= right:
    mid = (left + right) // 2
    value = house[0]
    cnt = 1

    for i in range(1, n):
        if house[i] >= value + mid:
            cnt += 1
            value = house[i]
    
    if cnt >= c:
        left = mid + 1
        result = mid
    else:
        right = mid - 1

print(result)