import sys
input = sys.stdin.readline

n, m = map(int, input().split())
word = list(input().split())
word.sort()

visit = [False] * m

answer = []

def dfs(cnt):
    if cnt == n:
        mo = 0
        za = 0
        for i in range(n):
            if answer[i] in 'aeiou':
                mo += 1
            else:
                za += 1
        if mo >= 1 and za >= 2:
            print(''.join(answer))
        

    for i in range(m):
        if visit[i]:
            continue
        visit[i] = True
        answer.append(word[i])
        dfs(cnt + 1)
        answer.pop()

        for j in range(i+1, m):
            visit[j] = False

dfs(0)
