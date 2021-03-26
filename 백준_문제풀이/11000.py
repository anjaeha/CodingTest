import heapq

n = int(input())
r = []
h = []

for i in range(n):
    r.append(list(map(int, input().split())))

r.sort(key = lambda x : x[0])

for i in range(n):
    if len(h) != 0 and h[0] <= r[i][0]:
        heapq.heappop(h)
    heapq.heappush(h, r[i][1])

print(len(h))
