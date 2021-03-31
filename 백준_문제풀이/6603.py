from itertools import combinations

while 1:
    k = list(map(int, input().split()))
    if k[0] == 0:
        break

    del k[0]

    answer = list(combinations(k, 6))
    
    for i in answer:
        for j in i:
            print(j, end = ' ')
        print()
    print()