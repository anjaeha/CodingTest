import sys
input = sys.stdin.readline

t = int(input())

for case in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    result = 0

    for i in range(2, n):
        result = max(result, abs(s[i] - s[i-2]))

    print(result)