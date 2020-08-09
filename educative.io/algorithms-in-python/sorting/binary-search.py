def binary_search(array, target, low, high):
    if low > high:
        return False

    middle = (high + low) // 2

    print(middle)
    if target == array[middle]:
        return True
    else:
        if target < array[middle]:
            high = middle-1
        
        else:
            low = middle+1
    
    return binary_search(array, target, low, high)


    
a = [0, 1, 2, 2, 3, 14, 22, 25, 35, 36, 36, 38, 39, 56, 3569]
print(binary_search(a, 77, 0, len(a)-1))