def find_sum_brute_force(lst, k):
    a = -1
    b = -1
    for index, first in enumerate(lst):
        for second in lst[index:]:
            if first + second == k:
                a = first
                b = second
                break
    return a, b

def binary_search(array, target):
    low = 0
    high = len(array) - 1
    found = False
    middle = -1

    while low < high and not found:
        middle = (high+low)//2

        if lst[middle] == target:
            found = True
        
        elif target < middle:
            high = middle - 1
        
        elif target > middle:
            low = middle + 1

    if not found:
        middle = -1

    return middle

def find_sum_binary_search(lst, k):
    a = -1
    b = -1

    lst.sort()
    for element in lst:
        target = k - element
        target_index = binary_search(lst, target)

        if target_index != -1:
            a = element
            b = target
            break
    
    return a, b


lst = [1,21,3,14,5,60,7,6]
k = 81

print(find_sum_binary_search(lst, k))


lst = [1,21,3,14,5,60,7,6,36,59,21,33,32,3,2,6,5,32,65,9889,312,0,2,3,6,6,6,6,3,2,5,6,45,95,98,326,5236,32659,2,3,25,24,28,29,27,232,26,39,95,96,98,86]
k = 33365236

print(find_sum_binary_search(lst, k))
