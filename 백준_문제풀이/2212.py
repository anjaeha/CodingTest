import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
s = list(map(int, input().split()))

s.sort()

if k >= n:
    print(0)
    exit()

dis = []
for i in range(n-1):
    dis.append(s[i+1] - s[i])

dis.sort(reverse=True)

for i in range(k-1):
    dis.pop(0)

print(sum(dis))