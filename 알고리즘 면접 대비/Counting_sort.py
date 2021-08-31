"""
Counting sort 계수정렬은?
    - 숫자들간 비교를 하지 않고 정렬하는 알고리즘.
    - 일일이 비교를 하는 것이 아닌, 각 숫자가 몇개인지 세어 정렬을 한다.
    그래서 시간 복잡도는 O(N)이 나온다. 하지만 일정한 조건을 만족해야 해당 알고리즘을 사용할 수 있다.
        1. 모든 요소들은 정수여야 한다.
        2. 모든 요소들은 0 ~ K 여야 한다.
        3. K = O(N)으로 나타나질 수 있어야 한다.

    시간 복잡도가 O(N)이라는 장점이 잇지만, K값이 커질 수록 다른 알고리즘으로 정렬하는 것이 빠를 수도 있다.
    또한 추가 메모리를 사용한다는 것도 단점.    
"""

def counting_sort(array, k):
    B = [0] * len(array)
    C = [0] * (k + 1)

    for i in range(len(array)): # 각 요소가 몇개 있는지를 C에 저장함.
        C[array[i]] += 1

    for i in range(1, len(C)): # C를 누적값으로 바꾼다.
        C[i] += C[i - 1]

    for i in range(len(array)): # C를 indexing해서 B에 저장
        B[C[array[i]] - 1] = array[i]
        C[array[i]] -= 1

    return B

array = [1, 0, 3, 1, 0, 2, 5, 1]
array = counting_sort(array, max(array))
print(array)


# 참고 : https://devjin-blog.com/sort-algorithm-8/