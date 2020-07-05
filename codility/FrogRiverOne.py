def solution(X, A):
    leafs = set()
    time = -1
    
    for index in range(len(A)):
        leaf = A[index]
        leafs.add(leaf)
        if len(leafs) == X:
            time = index
            break
    
    return time
