import sys
import heapq
input = sys.stdin.readline

n = int(input())
card = []
for i in range(n):
    heapq.heappush(card, int(input()))


result = 0

while len(card) != 1:
    one = heapq.heappop(card)
    two = heapq.heappop(card)

    sum_value = one + two
    result += sum_value

    heapq.heappush(card, sum_value)

print(result)