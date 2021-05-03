import sys
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())

t = []
for i in range(m):
    t.append(list(map(int, input().split())))

t.sort(key = lambda x : x[1])

answer = 0
remain = [c] * (n+1)

for i in range(m):
    temp = c
    for j in range(t[i][0], t[i][1]):
        temp = min(temp, remain[j])
    temp = min(temp, t[i][2])

    for j in range(t[i][0], t[i][1]):
        remain[j] -= temp

    answer += temp

print(answer)