n, c = map(int, input().split())

x = [int(input()) for _ in range(n)]
x.sort()

start = 1
end = x[-1] - x[0]

result = 0

while start <= end:
    mid = (start + end) // 2
    vlaue = x[0]
    cnt = 1

    for i in range(1, len(x)):
        if x[i] >= vlaue + mid:
            cnt += 1
            vlaue = x[i]
        
    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1



print(result)

# 다시 풀기
# https://solved.ac/search?query=tag%3Abinary_search+&sort=level&direction=asc&page=1