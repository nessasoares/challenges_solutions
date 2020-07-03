def solution(A, K):
    copy_A = A.copy()
    slice = copy_A[-K:]
    copy_A[-K:] = []
    
    
    return slice + copy_A
