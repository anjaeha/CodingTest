T = int(input())

cnt = 0

for case in range(T):
    word = input()
    if list(word) == sorted(word, key=word.find):
        cnt += 1
        
print(cnt)
