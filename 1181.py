N = int(input())

word_list = []

for case in range(N):
    word = str(input())
    word_cnt = len(word)
    word_list.append((word, word_cnt))

word_list = list(set(word_list))

word_list.sort(key = lambda word: (word[1], word[0]))

for i in word_list:
    print(i[0])



# lambda 이해하고 다시 풀어보기