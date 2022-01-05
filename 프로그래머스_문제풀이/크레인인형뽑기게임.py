def solution(board, moves):
    # 인형 뽑기 시작
    pick = []
    for move in moves:
        move -= 1
        for i in range(len(board)):
            if board[i][move] != 0:
                pick.append(board[i][move])
                board[i][move] = 0
                break
            else:
                continue
                
    answer = 0
    q = [-1]
    for i in range(len(pick)):
        if q[-1] != pick[i]:
            q.append(pick[i])
        else:
            q.pop()
            answer += 2
    return answer