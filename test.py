from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
MAX = 100001
time = [0] * MAX

def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()

        if x == k:
            print(time[x])
            return

        for i in (x-1, x+1, x*2):
            if 0 <= i < MAX and time[i] == 0:
                time[i] = time[x] + 1
                q.append(i)
bfs()