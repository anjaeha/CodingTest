import sys
input = sys.stdin.readline

card = []
color = [0, 0, 0, 0]
number = [0,0,0,0,0,0,0,0,0,0]

for i in range(5):
    card.append(list(input().split()))

for i in range(5):
    card[i][1] = int(card[i][1])

card.sort(key = lambda x:x[1])

for i in range(5):
    if card[i][0] == 'R':
        color[0] += 1
    elif card[i][0] == 'B':
        color[1] += 1
    elif card[i][0] == 'Y':
        color[2] += 1
    elif card[i][0] == 'G':
        color[3] += 1

for i in range(5):
    number[card[i][1]] += 1

# 규칙 1
# 5장이 같은색이면서 연속 => 가장 높은 숫자 + 900
if max(color) == 5 and card[0][1] + 4 == card[1][1] + 3 == card[2][1] + 2 == card[3][1] + 1 == card[4][1]:
    print(card[4][1] + 900)
    exit()

# 규칙 2
# 4장이 같은 숫자 => 같은 숫자 + 800
if max(number) == 4:
    print(number.index(max(number)) + 800)
    exit()

# 규칙 3
# 3장의 숫자 같음, 나머지 2장의 숫자 같음 => 3장 숫자 * 10 + 2장의 숫자 + 700
if 3 in number and 2 in number:
    print(number.index(3) * 10 + number.index(2) + 700)
    exit()

# 규칙 4
# 5장의 카드 색이 같음 => 가장 높은 숫자 + 600
if max(color) == 5:
    print(card[4][1] + 600)
    exit()

# 규칙 5
# 카드 5장이 연속 => 가장 높은 숫자 + 500
if card[0][1] + 4 == card[1][1] + 3 == card[2][1] + 2 == card[3][1] + 1 == card[4][1]:
    print(card[4][1] + 500)
    exit()

# 규칙 6
# 3장이 같은 숫자 => 같은 숫자 + 400
if 3 in number:
    print(number.index(3) + 400)
    exit()

# 규칙 7
# 2장, 2장 숫자 같음 => 큰 수 * 10 + 작은 수 + 300
cnt = []
for i in range(10):
    if number[i] == 2:
        cnt.append(i)

if len(cnt) == 2:
    print(cnt[1] * 10 + cnt[0] + 300)
    exit()

# 규칙 8
# 2장이 숫자 같음 => 같은 숫자 + 200
if 2 in number:
    print(number.index(2) + 200)
    exit()

# 규칙 9
# 규칙에 해당하지 않음 => 가장 큰 수 + 100
print(card[4][1] + 100)