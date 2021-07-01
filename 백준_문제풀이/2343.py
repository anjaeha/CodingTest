import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = list(map(int, input().split()))

left = max(s)
right = sum(s)


while left <= right:
    mid = (left + right) // 2
    cnt = 0
    time = 0

    for i in s:
        if i + time > mid:
            cnt += 1
            time = 0
        time += i
    
    if time:
        cnt += 1


    if cnt > m:
        left = mid + 1
    else:
        right = mid - 1

print(left)