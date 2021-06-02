import sys
input = sys.stdin.readline

n = int(input())

num = [1] * 10

for i in range(n-1):
    for j in range(1, 10):
        num[j] = (num[j] + num[j-1]) % 10007

print(sum(num) % 10007)