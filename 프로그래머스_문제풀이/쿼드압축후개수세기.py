def solution(arr):
    answer = [0 ,0]
    n = len(arr)
    
    def div(x, y, n):
        init = arr[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != init:
                    nn = n // 2
                    div(x, y, nn)
                    div(x + nn, y, nn)
                    div(x, y + nn, nn)
                    div(x + nn, y + nn, nn)
                    return
                
        answer[init] += 1
        
    div(0, 0, n)
    return answer