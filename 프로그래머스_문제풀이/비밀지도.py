def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        one = bin(arr1[i])[2:].zfill(n)
        two = bin(arr2[i])[2:].zfill(n)
        temp = ''
        
        for j in range(n):
            if one[j] == '1' or two[j] == '1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
        
    return answer