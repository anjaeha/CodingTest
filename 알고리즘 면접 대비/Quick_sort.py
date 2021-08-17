"""
퀵정렬에 대한 설명
- 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 정렬
대부분 첫번째 데이터를 기준 데이터(Pivot)으로 설정함.


동작 예시
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
1. 0번째 값인 5로 피벗을 설정하고
2. 1번부터 순서대로 진행하며 피벗보다 큰 값을 찾음.
3. 끝값 (N번째 값)부터 역순으로 진행하며 피벗보다 작은 값 찾음
4. 2번위치와 3번위치를 서로 변경함
5. 2~4를 계속 진행하면 피벗(5)보다 작은 값들과 큰 값들로 나뉨. arr의 상태는 [1, 4, 2, 0, 3, 5 , 6, 9, 7, 8]로 되어있음
6. 5보다 작은 값들의 집합과 5보다 큰 값들의 집합으로 나누어 각 집합에서 피벗을 다시 설정하여 2번부터 진행

시간 복잡도
평균의 경우 O(NlogN)의시간 복잡도를 가지며 => 만약 배열의 길이가 31이면, 4번 연산한다 (둘로나눠 15, 다시나눠 7, 다시나눠 3, 마지막 1) 그래서 logn인데
                                            배열의 길이만큼 (N)만큼 진행하기 때문에 NlogN의시간 복잡도를 가진다.
최악의 경우 O(N^^2)의 시간 복잡도를 가짐. => 정렬된 배열에서 피벗을 최소값이나 최대값으로 잡을때
하지만 보통의 경우, 데이터들이 정렬되어 있지 않아서 어지간하면 빠르다고 해서 퀵정렬이다.
피벗을 0번으로 안잡고 중간 index로 잡으면 최악의 경우를 피할 수 있긴하다.
공간복잡도는 주어진 배열 안에서 교환(SWAP)을 통해 이루어지므로 O(N)이다.
"""
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

quick_sort(arr, 0, len(arr) - 1)
print(arr)