import heapq
def solution(n, works):
    answer = 0
    max_heap = []
    for work in works:
        heapq.heappush(max_heap, (-work, work))

    for i in range(n):
        work = heapq.heappop(max_heap)
        if work[1] == 0:
            break
        heapq.heappush(max_heap, (-work[1] + 1, work[1] - 1))

    for i in range(len(max_heap)):
        answer += max_heap[i][1] ** 2

    return answer