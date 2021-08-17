import sys
input = sys.stdin.readline

n = int(input())

word = [input().strip() for _ in range(n)]
a = [0 for _ in range(26)]

number = 9

for w in word:
    length = len(w)
    for i in range(length):
        temp = ord(w[i]) - 65
        a[temp] += 10 ** (length - i - 1)
            
a.sort(reverse=True)

result = 0
for i in range(26):
    result += a[i] * number
    number -= 1

print(result)