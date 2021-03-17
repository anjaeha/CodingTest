N = int(input())

cnt = 0
for i in range(1, N+1):
    cnt += len(str(i))

print(cnt) 

# 2256ms 시간 소요