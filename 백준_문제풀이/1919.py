import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()
a_cnt = [0] * 26
b_cnt = [0] * 26

for i in range(len(a)):
    a_cnt[ord(a[i]) - ord('a')] += 1

for i in range(len(b)):
    b_cnt[ord(b[i]) - ord('a')] += 1


cnt = 0
for i in range(0, 26):
    if a_cnt[i] != b_cnt[i]:
        cnt += abs(a_cnt[i] - b_cnt[i])

print(cnt)