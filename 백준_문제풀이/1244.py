import sys
input = sys.stdin.readline

n = int(input())
s = [-1]
s += list(map(int, input().split()))
num = int(input())

for i in range(num):
    gender, idx = map(int, input().split())
    if gender == 1:
        for j in range(n // idx):
            s[idx * (j+1)] ^= 1
    else:
        cnt = 0
        while 1:
            if idx - cnt < 1 or idx + cnt > n:
                break

            if s[idx - cnt] == s[idx + cnt]:
                cnt += 1
            else:
                break
        cnt -= 1
        for j in range(cnt * 2 + 1):
            s[idx - cnt + j] ^= 1


s.pop(0)

for i in range(len(s)):
    print(s[i], end = ' ')
    if i == 19 or i == 39 or i == 59 or i == 79:
        print()