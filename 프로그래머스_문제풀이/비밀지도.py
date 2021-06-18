def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []
    
    for i in arr1:
        map1.append(list(map(int, bin(i)[2:].zfill(n))))
    for i in arr2:
        map2.append(list(map(int, bin(i)[2:].zfill(n))))
    
    
    for i in range(n):
        temp = ""
        for j in range(n):
            if map1[i][j] == 1 or map2[i][j] == 1:
                temp += "#"
            else:
                temp += " "
        answer.append(temp)
        

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))