from math import ceil
n = int(input()) # 시험장의 수
a = list(map(int, input().split())) # 시험장에 있는 응시자의 수
b, c = map(int, input().split()) # 총감독관, 부감독관 감시 가능 수

result = 0

for case in range(n):
    result += 1
    temp = a[case] - b
    if temp <= 0:
        continue
    else:
        result += ceil(temp / c)

print(result)