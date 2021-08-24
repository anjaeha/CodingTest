import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
answer = []

def lower_bound(start, end, num):
    while start < end:
        mid = (start + end) // 2

        if answer[mid] < num:
            start = mid + 1
        else:
            end = mid
    return end


for num in s:
    if len(answer) == 0:
        answer.append(num)
        continue

    if answer[-1] < num:
        answer.append(num)
    else:
        idx = lower_bound(0, len(answer) - 1, num)
        answer[idx] = num

print(len(answer))