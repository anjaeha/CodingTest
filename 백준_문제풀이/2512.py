import sys
input = sys.stdin.readline

n = int(input())
money = sorted(list(map(int, input().split())))
budget = int(input())

left = 0
right = max(money)

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for i in money:
        cnt += i if mid >= i else mid
    
    if cnt <= budget:
        left = mid + 1
    else:
        right = mid - 1

print(right)