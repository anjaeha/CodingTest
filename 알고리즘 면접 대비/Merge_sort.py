"""
합병 정렬
 - 이름만 들어도 생소함이 느껴지는 합병정렬이다.
 - 들어가기에 앞써 분할정복에 대해서 알고 있어야한다.
 - 분할정복이란 ?
    > 문제를 작은 2개의 문제로 분리하고 각각을 해결한 다음, 결과를 모아서 원래의 문제를 해결하는 방법이다
 - 분할정복 방법을 사용하는 병합 정렬의 시간 복잡도는 퀵정렬과 동일한 O(NlogN)이다. 16크기의 배열을 8로, 4로, 2로, 1로 나눠서 정렬하기 때문!
 - 또한 최악의 경우에도 O(NlogN)의 시간 복잡도를 가진다.
"""

def merge_sort(arr):
    n = len(arr)

    if n <= 1:
        return
    
    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)

    i1, i2, ia = 0, 0, 0

    while i1 < len(left) and i2 < len(right):
        if left[i1] < right[i2]:
            arr[ia] = left[i1]
            i1 += 1
            ia += 1
        else:
            arr[ia] = right[i2]
            i2 += 1
            ia += 1
    
    while i1 < len(left):
        arr[ia] = left[i1]
        i1 += 1
        ia += 1
    
    while i2 < len(right):
        arr[ia] = right[i2]
        i2 += 1
        ia += 1
    

arr = [7, 4, 5, 1, 3]
merge_sort(arr)
print(arr)