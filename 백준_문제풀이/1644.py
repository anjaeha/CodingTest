import sys
input = sys.stdin.readline

def prime_list(n):
    s = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if s[i]:
            for j in range(i * 2, n, i):
                s[j] = False
    return [i for i in range(2, n) if s[i] == True]

n = int(input())
data = prime_list(n + 1)
length = len(data)
summary, end, result = 0, 0, 0

for i in range(length):
    while summary < n and end < length:
        summary += data[end]
        end += 1

    if summary == n:
        result += 1
    
    summary -= data[i]

print(result)