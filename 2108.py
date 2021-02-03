import sys
from collections import Counter

a = int(input())

arr = []

for i in range(a):
    arr.append(int(sys.stdin.readline()))

arr.sort()    
    
    
def mode(x):
    mode_dict = Counter(x)
    modes = mode_dict.most_common()
    if len(x) > 1 : 
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else : 
            mod = modes[0][0]
    else : 
        mod = modes[0][0]
    
    return mod

print(int(round(sum(arr) / a, 0)))
print(arr[a//2])
print(mode(arr))
print(arr[-1] - arr[0])


# sys.stdin.readline() 이 압도적으로빠름 500ms 정도차이?