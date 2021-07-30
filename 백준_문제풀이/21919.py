import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
max_num = max(data) + 1

def prime_num(num):
    check = [True] * num
    m = int(num ** 0.5)
    for i in range(2, m + 1):
        if check[i]:
            for j in range(i * 2, num, i):
                check[j] = False

    return [i for i in range(2, num) if check[i] == True]

prime = prime_num(max_num)
number = []
for i in range(n):
    if data[i] in prime:
        number.append(data[i])

number = set(number)

answer = 1
if number != set():
    for i in number:
        answer *= i
else:
    answer = -1
print(answer)