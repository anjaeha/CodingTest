import sys
input = sys.stdin.readline

n = int(input())

for case in range(n):

    word = input()

    for i in range(len(word) - 1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                n -= 1
                break

print(n)