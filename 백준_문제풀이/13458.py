n = int(input())  # 시험장의 개수
p = list(map(int, input().split()))  # 시험장에 있는 응시자의 수
b, c = map(int, input().split())  # 총감독관 감시 수, 부감독관 감시 수

answer = 0
for i in range(n):
    answer += 1
    temp = p[i]
    temp -= b

    if temp > 0:
        if temp % c == 0:
            answer += temp // c
        else:
            answer += temp // c + 1

print(answer)