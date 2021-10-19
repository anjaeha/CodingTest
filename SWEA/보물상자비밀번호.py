# 각 변에는 16진수가 적혀 있는 보물 상자가 있음.
# 시계방향으로 돌리며, 한번에 한칸씩 이동
# 비밀번호는, 보물 상자에 적힌 숫자로 만들 수 있는 모든 수 중, K번째로 큰 수를 10진수로 만든 수

T = int(input())

for tc in range(1, T + 1):
    n, k = map(int, input().split())
    number = list(input())
    # 회전시키는 횟수는 N // 4 - 2회로, 경우의 수는 총 N // 4 - 1이 나온다.
    num = n // 4
    candi = set()
    for case in range(num):
        for i in range(4):
            temp = ''.join(number[i * num:i*num+num])
            candi.add(temp)
        number.insert(0, number.pop())

    candi = sorted(candi)

    answer = candi[-k]
    result = int(answer, 16)
    print("#%d %d" %(tc, result))