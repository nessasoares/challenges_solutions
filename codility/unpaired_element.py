# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    unpaired = 0
    for number in A:
        counter = A.count(number)
        if counter % 2 != 0:
            unpaired = number
            break
    
    return unpaired