import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
data = sorted(list(map(int, input().split())))

left = 0
right = n - 1
result = 0

while left < right:
    if data[left] + data[right] == m:
        result += 1

    if data[left] + data[right] > m:
        right -= 1
    else:
        left += 1

print(result)