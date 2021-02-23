
for case in range(int(input())):
    n = int(input())
    s = [0 for _ in range(n+1)]
    cnt = 0

    for i in range(n):
        a, b = map(int, input().split())
        s[a] = b
    
    min_n = s[1]

    for j in range(2, n+1):
        if min_n < s[j]:
            cnt += 1
        else:
            min_n = s[j]

    print(n - cnt)