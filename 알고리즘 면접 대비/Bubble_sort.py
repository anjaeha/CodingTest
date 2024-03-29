"""
버블정렬은 서로 인접한 두 원소를 검사하여 정렬하는 알고리즘
 - 인접한 2개의 레코드를 비교하여 크기가 순서대로 되어 있지 않으면 서로 교환함.
arr = [7, 4, 5, 1, 3]라고 할때
    1. arr[0]과 arr[1]을 비교 => 7과 4를 비교하여 큰 값을 우측으로 => [4, 7, 5, 1, 3]으로 정렬됨
    2. 다음 arr[1]과 arr[2]를 비교 => 7과 5를 비교 => [4, 5, 7, 1, 3]으로 정렬됨.
    3. 다음 arr[2]와 arr[3]을 비교 => 7과 1을 비교 => [4, 5, 1, 7, 3]으로 정렬됨.
    4. 다음 arr[3]과 arr[4]를 비교 => 7과 3을 비교 => [4, 5, 1, 3, 7]으로 정렬됨.
    5. 그러면 맨 우측에 있는 7은 arr함수의 최대값임을 알 수 있다.
    6. 다시 1번으로 돌아가서 arr[3]까지만 비교하면됨. (arr[4]는 7로 최대값이기 때문에 비교할 필요 없음.)
버블 정렬은 위에 보는 것 처럼 처음에는 4번 비교하고, 3번, 2번, 1번 비교를 하게 된다. => N(N-1) / 2의 비교 횟수를 지니기 때문에
최악, 최상, 평균  모두 N ** 2의 시간복잡도를 가지게 된다.
매우 비효율적이지만 단순(구현하기 간단)한 함수
공간복잡도는 별도의 추가 공간을 사용하지 않고, 주어진 배열안에서 순서만 바꾸기 때문에 O(1)의 공간 복잡도를 가진다.
"""
arr = [7, 4, 5, 1, 3]
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubble_sort(arr)
print(arr)