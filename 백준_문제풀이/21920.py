import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
x = int(input())

answer = []

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

for i in data:
    temp = gcd(x, i)
    if temp == 1:
        answer.append(i)

print(sum(answer) / len(answer))