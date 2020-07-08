def solution(A):
    array = set(A)
    array.add(0)
    missing = 0
    
    for i in range(len(array)):
        if i != array[i]:
            missing = array[i] - 1
            break
        
    return missing