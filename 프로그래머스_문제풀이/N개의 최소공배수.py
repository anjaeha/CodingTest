def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def solution(arr):
    answer = 0
    while len(arr) > 1:
        a = arr.pop()
        b = arr.pop()
        arr.append(a * b // gcd(a, b))
    return arr[0]