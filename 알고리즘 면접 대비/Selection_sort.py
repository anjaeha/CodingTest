"""
선택정렬은 주어진 배열 중에 최소값을 찾고, 그 값의 위치를 맨 앞에 위치한 값과 교체함.
그 다음 맨 처음 위치를 뺀 나머지 배열을 같은 방법으로 교체한다.
쉽게 말해, 하나의 값을 '선택'하고 그 값의 위치를 찾은 뒤, 다른 값을 '선택'하는 방식

시간복잡도는 당연하게도 O(N ** 2)를 가지며, 주어진 배열안에서 교체하기 때문에 O(N)의 공간복잡도를 가진다.
버블정렬과 비슷하게 구현하기가 매우 편하며, 공간복잡도가 좋다.
하지만 시간복잡도가 O(N ** 2)인것이 매우 비효율적이다.
"""


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]: # 가장 작은 값을 찾는 중..
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # 가장 작은 값과 arr[i]의 위치를 변경해준다.

    return arr

arr = [7, 4, 5, 1, 3]
selection_sort(arr)
print(arr)