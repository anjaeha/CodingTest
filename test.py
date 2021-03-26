import heapq

n = int(input())
r = []
h = []

for i in range(n):
    r.append(list(map(int, input().split())))

r.sort(key = lambda x : x[0])

cnt = 0
end = r[0][1]

for i in range(n):
    if end <= r[i][0]:
        end = r[i][1]
        cnt += 1

print(cnt + 1)
