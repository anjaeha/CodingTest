s = input()
boom = input()
length = len(boom)
stack = []

for i in s:
    stack.append(i)
    if i == boom[-1] and ''.join(stack[-length:]) == boom:
        for _ in range(length):
            stack.pop()

answer = ''.join(stack)
print(answer if answer else "FRULA")