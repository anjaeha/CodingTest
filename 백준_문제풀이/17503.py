from heapq import heappop, heappush

n, m, k = map(int, input().split())
beers = [list(map(int, input().split())) for _ in range(k)]

# 선호도 M을 채우며 N개의 맥주를 마실 수 있는 간 레벨의 최솟값
beers.sort(key = lambda x : (x[1], x[0]))
satis = 0
heap = []

for beer in beers:
    satis += beer[0]
    heappush(heap, beer[0])

    if len(heap) == n:
        if satis >= m:
            answer = beer[1]
            break
        else:
            satis -= heappop(heap)
else:
    answer = -1

print(answer)