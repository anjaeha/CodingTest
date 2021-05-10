import sys
input = sys.stdin.readline

score = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]
count = []
word = list(input().strip())

for i in word:
    count.append(score[(int(ord(i) - ord('A')))])

if sum(count) % 2 == 0:
    print('You\'re the winner?')
else:
    print('I\'m a winner!')