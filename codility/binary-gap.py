def solution(N):
    max_gap = 0
    binary_n = "{0:b}".format(N)
    gap_size = 0
    for digit in binary_n:
        if digit == '0':
            gap_size +=1
        else:
            if gap_size > max_gap:
                max_gap = gap_size
            gap_size = 0
    return max_gap
    
