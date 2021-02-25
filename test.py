n = int(input())

room = [list(map(int, input().split())) for i in range(n)]

room.sort(key = lambda x : (x[1], x[0]))

cnt = 0
end = 0

for i in room:
    if end <= i[0]:
        cnt += 1
        end = i[1]

print(cnt)