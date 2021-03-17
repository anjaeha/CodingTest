from math import gcd

N = int(input())

num = list(map(int, input().split()))
# 링의 크기 입력받아서

main = num[0]
rest = num[1:]
# 첫번째링과 나머지 링 입력받기

arr = []
# 기약 분수형태로 출력해야하기 때문에 최대 공약수 입력받을 arr 선언

for i in range(len(rest)):
    arr.append(gcd(rest[i], main))
    # 최대 공약수 찾아서 arr에 입력해놓기

for i in range(len(rest)):
    print("%d/%d" %(main//arr[i], rest[i]//arr[i]))
    # 첫번째링과 나머지링 최대공약수로 나눠서 기약 분수형태로 출력