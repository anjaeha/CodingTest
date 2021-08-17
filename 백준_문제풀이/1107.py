import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
disable_number = list(map(int, input().split()))
able_number = set([i for i in range(0, 10)])

for i in range(m):
    able_number.remove(disable_number[i])

min_count = abs(100 - n)

for num in range(1000001):
    num = str(num)
    for i in num:
        if int(i) in disable_number:
            break
    else:
        min_count = min(min_count, len(num) + abs(int(num) - n))

print(min_count)