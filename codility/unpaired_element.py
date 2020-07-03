from collections import Counter
def solution_1(A):
    unpaired = 0
    for number in A:
        counter = A.count(number)
        if counter % 2 != 0:
            unpaired = number
            break
    
    return unpaired

def solution_2(A):
    counter = Counter(A)
    for item in counter.items():
        if item[1] % 2 > 0:
            return item[0]
