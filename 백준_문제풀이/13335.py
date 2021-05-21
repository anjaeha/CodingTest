import sys
input = sys.stdin.readline

n, w, l = map(int, input().split())
truck = list(map(int, input().split()))

bridge = l
s = [0 for _ in range(n)]
cnt = 0
start = 0
end = 0

while 1:
    cnt += 1

    for i in range(start, end):
        s[i] += 1

        if s[i] > w:
            bridge += truck[i]
            start += 1

    if start == n:
        break

    if end < n:
        if truck[end] <= bridge:
            bridge -= truck[end]
            s[end] += 1
            end += 1

print(cnt)