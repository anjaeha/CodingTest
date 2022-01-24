def solution(files):
    answer = []
    for file in files:
        head, number, tail = '', '', ''
        flag = False
        for f in range(len(file)):
            if not flag and not file[f].isdigit():
                head += file[f]
            elif file[f].isdigit():
                number += file[f]
                flag = True
            else:
                tail += file[f:]
                break
        answer.append((head, number, tail))

        
    answer.sort(key = lambda x : (x[0].lower(), int(x[1])))
    
    result = []
    for i in answer:
        result.append(''.join(i))
    return result