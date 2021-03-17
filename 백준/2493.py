import sys
input = sys.stdin.readline

T = int(input())
tower = list(map(int, input().split()))
answer = [0] * T
stack = []

for i in range(T):
    n = tower[i]

    while stack and tower[stack[-1]] < n:
        stack.pop()
    if stack:
        answer[i] = stack[-1] + 1

    stack.append(i)

print(*answer)