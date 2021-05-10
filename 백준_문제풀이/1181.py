import sys
input = sys.stdin.readline

n = int(input())

word = []
for i in range(n):
    word.append(input().strip())

word.sort(key = lambda x : (len(x), x))
answer = []
for v in word:
    if v not in answer:
        answer.append(v)

for i in answer:
    print(i)