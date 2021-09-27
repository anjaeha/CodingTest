T = int(input()) # 테스트케이스 개수

for case in range(T):
    n, m, k, a, b = map(int, input().split())
    ai = list(map(int, input().split()))
    bj = list(map(int, input().split()))
    tk = list(map(int, input().split()))

    result = 0
    if n == 1 and m == 1:
        for c in range(1, k + 1):
            result += c
        print("#%d %d" %(case + 1, result))
        continue
    
    use_A = []
    use_B = []
    wait_re = []
    receipt = [[0, 0] for _ in range(n)] #번호와 들어간 시간
    fix = [[0, 0] for _ in range(m)]
    wait_fix = []
    cnt_done = 0

    t = 0
    c = 1
    while cnt_done < k: # 끝낸 사람의 수
        for i in range(m):
            if fix[i][0] != 0 and fix[i][1] == t - bj[i]: # 정비가 끝난 곳이 있으면 초기화
                fix[i] = [0, 0]
                cnt_done += 1
        
        for i in range(n):
            if receipt[i][0] != 0 and receipt[i][1] == t - ai[i]: # 접수가 끝난 곳이 있으면 정비 대기열에 넣어줌
                wait_fix.append(receipt[i][0])
                receipt[i] = [0, 0]
                
        for i in range(len(tk)): # 0초부터 tk와 일치하는 값이 있으면 접수 대기열에 넣어줌
            if tk[0] == t:
                wait_re.append(c)
                del tk[0]
                c += 1
        
        for i in range(n):
            if receipt[i] == [0, 0] and wait_re: # 접수 창구에 빈자리가 있고 대기열이 있으면 넣어줌
                receipt[i] = [wait_re.pop(0), t]
                if i + 1 == a:
                    use_A.append(receipt[i][0])
        
        for i in range(m):
            if fix[i] == [0, 0] and wait_fix: # 정비 창구에 빈자리가 있고 대기열이 있으면 넣어줌
                fix[i] = [wait_fix.pop(0), t]
                if i + 1 == b:
                    use_B.append(fix[i][0])
        t += 1

    for i in use_A:
        if i in use_B:
            result += i
    
    if result != 0:
        print("#%d %d" %(case + 1, result))
    else:
        print("#%d %d" %(case + 1, -1))