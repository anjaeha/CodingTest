def solution(board, moves):
    answer = 0
    doll = []
    
    b = [[] for _ in range(len(board[0]))]
    
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[j][i] != 0:
                b[i].append(board[j][i])
    
    for i in moves:
        if b[i-1] == []:
            continue
        else:
            temp = b[i-1].pop(0)
            if doll == []:
                doll.append(temp)
            else:
                if temp == doll[-1]:
                    del doll[-1]
                    answer += 2
                else:
                    doll.append(temp)
        
            
    
    return answer