def solution(arr):
    
    idx = arr[0]

    if len(arr) > 1:
        for i in range(1, len(arr)):
            idx = (arr[i] * idx) // gcd(idx, arr[i])

    return idx


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

print(solution([2,6,8,14]))