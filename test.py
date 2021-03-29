from collections import Counter

n = int(input())

def fact(n):
    if n == 1:
        return  1

    return n * fact(n-1)

num = fact(n)

cnt = 0

while num % 10 == 0:
    num //= 10
    cnt += 1

print(cnt)