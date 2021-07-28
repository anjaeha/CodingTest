import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

left = 0
right = n - 1
result = 2000000001
answer = []

while left < right:
    s_left = data[left]
    s_right = data[right]

    hap = s_left + s_right

    if abs(hap) < result:
        result = abs(hap)
        answer = [s_left, s_right]

    if hap < 0:
        left += 1
    else:
        right -= 1

print(*answer)