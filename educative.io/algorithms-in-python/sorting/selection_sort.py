def selectionSort(lst):
    array_size = len(lst)
    for index_i in range(array_size):
        min_index = index_i

        for index_j in range(index_i+1, array_size-1):
            if lst[index_j] < lst[min_index]:
                min_index = index_j

        lst[index_i], lst[min_index] = lst[min_index], lst[index_i]
    return lst

print(selectionSort([5,3,8,6,9,2,1,4,7,10]))