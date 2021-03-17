sosu = [0 for i in range(10001)]
sosu[1] = 1

for i in range(2, 10001):
    for j in range(i*2, 10001, i):
        sosu[j] = 1
# 1이면 소수 만들어놓음

for i in range(int(input())):
    a = int(input())
    b = a // 2

    for j in range(b, 1, -1):
        if sosu[j] == 0 and sosu[a-j] == 0:
            print(j, a-j)
            break