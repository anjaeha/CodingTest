"""
이분 탐색
    - 탐색 범위를 두 부분으로 분할하여 찾는 방식
    - 전체 탐색하는데 시간복잡도가 O(N)인데, 이분탐색은 O(logN)이다.
    
    - 정렬방법이 아닌, 탐색 방법
    - 이분 탐색을 하기 위해서는 정렬이 되어있어야한다.
"""

def binary_search(array, x):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == x:
            return mid
        
        if array[mid] > x:
            right = mid - 1
        else:
            left = mid + 1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(arr, 5)
print(result)