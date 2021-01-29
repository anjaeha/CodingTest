T = int(input())

for i in range(T):
    grade = list(map(int, input().split()))

    n = grade[0]
    grade = grade[1:]

    average = sum(grade) / n

    cnt = 0
    for i in grade:
        if i > average:
            cnt += 1

    per = cnt / n * 100

    print("%.3f%%" %(round(per, 3)))