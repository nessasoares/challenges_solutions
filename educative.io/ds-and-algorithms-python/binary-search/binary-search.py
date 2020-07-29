def binary_search(array, target):
    low_index = 0
    high_index = len(array) - 1

    while low_index <= high_index:
        middle_element = (low_index + high_index) // 2

        if target == middle_element:
            return True
        elif target < array[middle_element]:
            high_index = middle_element - 1 
        else:
            low_index = middle_element + 1

        return False

def recursive_binary_search(array, target, low_index, high_index):
    if low_index > high_index:
        return False
    else:
        
        middle_element = (low_index + high_index) // 2

        if target == array[middle_element]:
            return True
        elif target < array[middle_element]:
            high_index = middle_element - 1
        else:
            low_index = middle_element + 1
        
        return recursive_binary_search(array, target, low_index, high_index)