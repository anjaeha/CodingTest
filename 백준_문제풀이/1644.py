import sys
input = sys.stdin.readline

n = int(input())
prime = []
array = [False, False] + [True] * (n-1)

for i in range(2, n+1):
    if array[i]:
        prime.append(i)
    for j in range(i*2, n+1, i):
        array[j] = False

print(prime)

start = 0
end = 0
cnt = 0
interval_sum = 0

while True:
    if interval_sum >= n:
        if interval_sum == n:
            cnt += 1
        interval_sum -= prime[start]
        start += 1
    elif end == len(prime):
        break
    else:
        interval_sum += prime[end]
        end += 1

print(cnt)