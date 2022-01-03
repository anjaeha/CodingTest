import sys
sys.setrecursionlimit(10 ** 4)

def postOrder(start, end):
    if start > end:
        return
    
    root = preOrder[start]
    idx = start + 1

    while idx <= end:
        if preOrder[idx] > root:
            break
        idx += 1
    
    postOrder(start + 1, idx - 1)
    postOrder(idx, end)
    print(root)


preOrder = []
while 1:
    try:
        preOrder.append(int(input()))
    except:
        break

postOrder(0, len(preOrder) - 1)