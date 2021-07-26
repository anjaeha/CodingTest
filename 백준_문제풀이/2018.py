import sys
input = sys.stdin.readline

n = int(input())
arr = [i for i in range(1, n+1)]

now = 0
end = 0
ans = 0

for s in range(n):
    while end < n and now < n:
        now += arr[end]
        end += 1
    
    if now == n:
        ans += 1
    
    now -= arr[s]

print(ans)