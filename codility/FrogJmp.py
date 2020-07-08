def solution(X, Y, D):
    difference_distance = Y - X
    total_jumps = (difference_distance // D)
    if difference_distance % D > 0:
        total_jumps += 1

    return total_jumps
