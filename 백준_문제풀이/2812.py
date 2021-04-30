import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(input())

stack = []
K = k
for i in range(n):
    while k > 0 and stack and stack[-1] < s[i]:
        stack.pop()
        k -= 1
    
    stack.append(s[i])

print(''.join(stack[:n-K]))