T = int(input())

for case in range(T):
    p = input()
    q = input()

    if p + 'a' == q:
        print('#%d N' %(case+1))
    else:
        print('#%d Y' %(case+1))

# 100개중 76개 맞음;; 'a'추가하는거 말고 뭐있을까?