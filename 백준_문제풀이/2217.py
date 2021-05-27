import sys
input = sys.stdin.readline

n = int(input())
rope = []
for i in range(n):
    rope.append(int(input()))
rope.sort()
weight = []
weight += rope

for i in range(n):
    weight.append(rope[i] * (len(rope) - i))

print(max(weight))