def solution(brown, yellow):
    syn = brown + yellow
    # 약수 구하기
    candi = []
    
    for i in range(1, syn // 2 + 1):
        if syn % i == 0:
            candi.append(i)
    
    for row in candi:
        col = syn // row
        # 가로 길이는 세로 길이보다 크거나 같다.
        if row >= col:
            if col * 2 + (row - 2) * 2 == brown:
                return [row, col]