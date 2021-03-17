n = int(input())
arr = []


for i in range(n):
    word = input()
    word_cnt = len(word)
    arr.append((word, word_cnt))

arr = list(set(arr))

arr.sort(key = lambda x : (x[1], x[0]))

for i in arr:
    print(i[0])