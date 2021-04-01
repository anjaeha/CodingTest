import sys
input = sys.stdin.readline

s = [0 for _ in range(1000000)]
s[0] = 1
s[1] = 2
s[2] = 4

for i in range(3, 1000000):
        s[i] = s[i-3] % 1000000009 + s[i-2] % 1000000009 + s[i-1] % 1000000009


for case in range(int(input())):
    n = int(input())
    
    print(s[n-1] % 1000000009)

