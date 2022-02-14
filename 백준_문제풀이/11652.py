n = int(input())

card = {}
for i in range(n):
    x = int(input())
    if x in card:
        card[x] += 1
    else:
        card[x] = 1

card = sorted(card.items(), key = lambda x : (-x[1], x[0]))
print(card[0][0])