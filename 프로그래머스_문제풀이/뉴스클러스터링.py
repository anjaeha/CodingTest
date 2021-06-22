def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1_lst = []
    str2_lst = []
    ans1 = []
    ans2 = []
    andset = []
    
    for i in range(1, len(str1)):
        str1_lst.append(str1[i-1:i+1])
    for i in range(1, len(str2)):
        str2_lst.append(str2[i-1:i+1])

    for i in str1_lst:
        if i.isalpha():
            ans1.append(i)

    for i in str2_lst:
        if i.isalpha():
            ans2.append(i)
    
    
    if len(ans1) > len(ans2):
        temp = ans2
        ans2 = ans1
        ans1 = temp
    
    idx = 0
    length1 = len(ans1)
    length2 = len(ans2)
    for i in range(len(ans1)):
        if ans1[idx] in ans2:
            temp = ans1[idx]
            andset.append(temp)
            ans1.remove(temp)
            ans2.remove(temp)
        else:
            idx += 1

    if length1 == 0 and length2 == 0:
        return 65536
    elif length1 == 0 or length2 == 0:
        return 0
    else:
        return int(65536 * len(andset) / (length1 + length2 - len(andset)))

print(solution("handshake", "shake hands"))