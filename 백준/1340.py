time = input().split()

M = time[0]
D = int(time[1].split(',')[0])
Y = int(time[2])
H = int(time[3].split(":")[0])
Mi = int(time[3].split(":")[1])

mon = 0
if M == 'January':
    mon = 1
elif M == 'February':
    mon = 2
elif M == 'March':
    mon = 3
elif M == 'April':
    mon = 4
elif M == 'May':
    mon = 5
elif M == 'June':
    mon = 6
elif M == 'July':
    mon = 7
elif M == 'August':
    mon = 8
elif M == 'September':
    mon = 9
elif M == 'October':
    mon = 10
elif M == 'November':
    mon = 11
elif M == 'December':
    mon = 12

Days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

Check = False # 윤년 체크
if Y % 400 == 0 or (Y % 4 == 0 and Y % 100 != 0):
    Check = True

# 1년 분으로 변환
if Check == False:
    total = 365 * 24 * 60
else:
    total = 366 * 24 * 60


sum = 0
for i in range(mon-1):
    if i == 1 and Check == True:
        sum = sum + 29
        continue
    sum += Days[i]
sum += D

InputTotal = (sum-1) * 24 * 60 + (H * 60 + Mi)
print(InputTotal / total * 100)

# 해당 달 전까지 날짜수를 다 더하고 시간 더하면 됨. 