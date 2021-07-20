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
    
    return [''.join(k) for k in answer]

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution( ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))


"""
import re
def solution(files):
    file_lst = [re.split('([0-9]+)',i) for i in files]
    file_lst.sort( key = lambda x : ( x[0].lower(), int(x[1]) ) )

    return [''.join(lst) for lst in file_lst]
# 정규 표현식
[a-c] : [abc]와 같음
[0-5] : [012345]와 같음
[a-zA-Z] : 모든 알파벳
[0-9] : 숫자
[^]면 반대를 뜻한다.
1o*1 면 1와 1사이에 o가 0개 이상이면 매치됨. 중간에 이상한거 하나라도 끼면 불일치
1o+1면 1와 1사이에 o가 1개 이상이여야 함, 
1o?1면 1개 있거나 없을때 매치
1o{3, 5}1 면 o가 3번이상 5번 이하일때 매치
"""