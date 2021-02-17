

n, m = map(int, input().split())

num = [i+1 for i in range(n)]
# 1부터 n까지 배열을 만들어놓고
check = [False] * n
# 중복검사를 위한 check
arr = []
# 답을 출력하기 위한 배열 선언

def dfs(cnt):
    if (cnt == m):
    # cnt(저장한 숫자)가 m과 같으면 arr출력하면서 종료
        print(*arr)
        return
    
    for i in range(0, n):
        if(check[i]):
        # i가 True 면 중복되면 안되기때문에 continue
            continue
        check[i] = True
        arr.append(num[i])
        dfs(cnt + 1)
        arr.pop()

        check[i] = False

dfs(0)