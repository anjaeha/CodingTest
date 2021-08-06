import sys
input = sys.stdin.readline

s = [i for i in range(1, 21)]

for i in range(10):
    x, y = map(int, input().split())
    temp = s[x-1:y]
    temp.reverse()
    s = s[:x-1] + temp + s[y:]

print(*s)