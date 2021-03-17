A, B, C = map(int, input().split())
cost = 0

if C > B:
    cost = A // (C-B) + 1
else:
    cost = -1

print(cost)