s = input().split('-')

num = []
for i in s:
    cnt = 0
    for j in i.split('+'):
        cnt += int(j)
    num.append(cnt)



result = num[0]
for i in range(1, len(num)):
    result -= num[i]

print(result)