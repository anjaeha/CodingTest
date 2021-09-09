n = int(input())

book = dict()

for i in range(n):
    sell_book = input()
    if sell_book in book:
        book[sell_book] += 1
    else:
        book[sell_book] = 1

book = sorted(book.items(), key = lambda x : x[1], reverse=True)

maxVal = book[0][1]
bestSeller = []

for key, val in book:
    if val == maxVal:
        bestSeller.append(key)

bestSeller.sort()

print(bestSeller[0])