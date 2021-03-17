l, c = map(int, input().split())

arr = list(map(str, input().split()))
arr.sort()

check = [False] * c

answer = []
t = []

def dfs(cnt):
    if (cnt == l):
        za = 0
        mo = 0

        for i in range(l):
            if answer[i] in 'aeiou':
                mo += 1
            else:
                za += 1

        if za >= 2 and mo >= 1:
            print(''.join(answer))


    for i in range(c):
        if (check[i]):
            continue

        check[i] = True
        answer.append(arr[i])
        dfs(cnt+1)
        answer.pop()

        for j in range(i+1, c):
            check[j] = False

dfs(0)