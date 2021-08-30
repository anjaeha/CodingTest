"""
힙정렬
 - 완전 이진 트리를 기본으로 하는 힙(Heap) 자료구조를 기반으로한 정렬 방식
 - 힙정렬은 최소힙/최대힙으로 이루어져 있는데, 루트에는 항상 최소/최대값이다.
 - 그래서 최소/최대값부터 순서대로 빼주는 방식을 사용하기 때문에 O(NlonN)의 시간 복잡도를 가진다.
"""

import heapq

def heap_sort(arr):
    result = []
    heap = []

    for value in arr:
        heapq.heappush(heap, value)

    for i in range(len(heap)):
        result.append(heapq.heappop(heap))

    return result

arr = [1,8,3,4,7,6,9,0]

arr = heap_sort(arr)

print(arr)