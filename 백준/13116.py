T = int(input())

answer = []
for i in range(T):
    A, B = map(int, input().split())

    while not A == B:
        if A > B: 
            A //= 2
        else: 
            B //= 2
    
    answer.append(A * 10)

for i in answer:
    print(i)