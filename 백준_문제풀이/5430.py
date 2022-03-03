from collections import deque
import sys
input=lambda: sys.stdin.readline().rstrip()

t = int(input())

for tc in range(t):
    order = list(input())
    n = int(input())
    temp = input()
    temp = temp[1:-1].split(',')
    numbers = deque()
    for i in range(len(temp)):
        if temp[i] != '':
            numbers.append(temp[i])

    flag = True # 오름차순인지 확인
    result = True # 중간에 에러가 나는지 확인

    for i in order:
        if i == 'R':
            flag = not flag
        elif i == 'D':
            if numbers:
                if flag:
                    numbers.popleft()
                else:
                    numbers.pop()
            else:
                result = False
                break


    if result: # 에러가 없으면
        if flag: # 오름차순 일때
            temp = (list(numbers))
        else: # 역순일 때
            temp = (list(numbers)[::-1])
        if temp:
            answer = '[' + ','.join(temp) + ']'
        else:
            answer = '[]'
        print(answer)
    else:
        print("error")