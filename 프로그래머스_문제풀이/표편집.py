def solution(n, k, cmd):
    arr = {}
    for i in range(1, n + 1):
        arr[i] = [i - 1, i + 1]

    answer = ['O'] * n
    cur = k
    stack = []

    cur += 1

    for c in cmd:
        if len(c) > 1:
            temp = c.split()
            val = int(temp[1])
            if temp[0] == 'D':
                for _ in range(val):
                    cur = arr[cur][1]
            elif temp[0] == 'U':
                for _ in range(val):
                    cur = arr[cur][0]
        else:
            if c == 'C':
                left, right = arr[cur]
                stack.append([left, cur, right])
                answer[cur - 1] = 'X'

                if right == n + 1:
                    cur = arr[cur][0]
                else:
                    cur = arr[cur][1]
                if left == 0:
                    arr[right][0] = left
                elif right == n + 1:
                    arr[left][1] = right
                else:
                    arr[right][0] = left
                    arr[left][1] = right

            elif c == 'Z':
                if stack:
                    left, now, right = stack.pop()
                    answer[now - 1] = 'O'

                    if left == 0:
                        arr[right][0] = now
                    elif right == n + 1:
                        arr[left][1] = now
                    else:
                        arr[right][0] = now
                        arr[left][1] = now

    result = ''
    for x in answer:
        result += x
    return result


# https://programmers.co.kr/learn/courses/30/lessons/81303