import sys
input = sys.stdin.readline

n = list(input().strip())
m = int(input())
number = [True] * 10
answer = abs(100 - int(''.join(n)))

temp = list(map(int, input().split()))
for i in range(m):
    number[temp[i]] = False

for num in range(1000001):
    num = str(num)
    for j in range(len(num)):
        if not number[int(num[j])]:
            break
        elif j == len(num) - 1:
            answer = min(answer, abs(int(''.join(n))-int(num)) + len(str(num)))

print(answer)