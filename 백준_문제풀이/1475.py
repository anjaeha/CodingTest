import sys
import math
input = sys.stdin.readline

n = input().strip()
number = [0] * 10

sixnine = 0
for i in range(10):
    if i == 6 or i == 9:
        sixnine += n.count(str(i))
    else:
        number[i] = n.count(str(i))

print(max(max(number), math.ceil(sixnine / 2)))