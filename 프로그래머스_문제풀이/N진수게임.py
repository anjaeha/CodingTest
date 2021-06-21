def solution(n, t, m, p):
    
    def conver(n, base):
        arr = "0123456789ABCDEF"
        q, r = divmod(n, base)
        if q == 0:
            return arr[r]
        else:
            return conver(q, base) + arr[r]
    
    answer = ''
    cnt = []

    for i in range(t * m):
        conv = conver(i, n)
        for c in conv:
            cnt.append(c)


    for i in range(p-1, t * m, m):
        answer += cnt[i]
    
    return answer
    
print(solution(16, 16, 2, 1))
print(solution(2, 4, 2, 1))