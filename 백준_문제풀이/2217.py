import sys
input = sys.stdin.readline

n = int(input())
rope = []

for i in range(n):
    rope.append(int(input()))

weight = []
rope.sort(reverse=True)

for i in range(n):
    weight.append(rope[i] * (i+1))

print(max(weight))