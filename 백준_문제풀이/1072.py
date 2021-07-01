import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = int(100 * y / x)

left = 0
right = x

if z >= 99:
    print(-1)
else:
    while left <= right:
        mid = (left + right) // 2

        nx = x + mid
        ny = y + mid

        if int(100 * ny / nx) > z:
            right = mid - 1
        else:
            left = mid + 1

    print(left)