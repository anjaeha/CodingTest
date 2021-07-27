import sys
input = sys.stdin.readline

n, m = map(int, input().split())
one = list(map(int, input().split()))
two = list(map(int, input().split()))
number = []

up = 0
down = 0

while up < n and down < m:
    if one[up] < two[down]:
        number.append(one[up])
        up += 1
    else:
        number.append(two[down])
        down += 1

while up < n:
    number.append(one[up])
    up += 1
while down < m:
    number.append(two[down])
    down += 1


print(*number)