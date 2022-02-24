def solution(n, k, cmd):
    arr = {}
    for i in range(1, n + 1):
        arr[i] = [i - 1, i + 1]

    answer = ['O'] * n
    stack = []
    cur = k

    cur += 1

    for c in cmd:
        if len(c) > 1:
            temp = c.split()
            if temp[0] == 'D':  # 아래로 이동
                for _ in range(int(temp[1])):
                    cur = arr[cur][1]
            elif temp[0] == 'U':  # 위로 이동
                for _ in range(int(temp[1])):
                    cur = arr[cur][0]
        else:
            if c[0] == 'C':  # 삭제
                left, right = arr[cur]
                stack.append([left, cur, right])
                answer[cur - 1] = 'X'

                if right == n + 1:  # 마지막 위치에서 삭제될때만 위로 이동
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
            elif c[0] == 'Z':  # 복구
                if stack:
                    left, now, right = stack.pop()
                    answer[now - 1] = 'O'

                    if left == 0:
                        arr[right][0] = now
                    elif right == n + 1:
                        arr[left][1] = now
                    else:
                        arr[left][1] = now
                        arr[right][0] = now
    result = ''
    for x in answer:
        result += x

    return result

