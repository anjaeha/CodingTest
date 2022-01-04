# 홀 > 짝, 숫자 큰거 순서대로
number = list(map(int, input().split()))

flag = False
answer = 1
for num in number:
    if num % 2 != 0:
        answer *= num
        flag = True
if not flag:
    for num in number:
        answer *= num

print(answer)