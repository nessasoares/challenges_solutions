def bubble_sort(lst):
    is_not_sorted = False
    array_size = len(lst)
    index = 0

    while not is_not_sorted:
        changed = False 
        for i in range(array_size-1):
            if i+1 >= array_size:
                continue
            
            current = lst[i]
            next = lst[i+1]

            if next < current:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                changed = True
        print(lst)
        if not changed:
            is_not_sorted = True

    return lst

print(bubble_sort([5,3,8,6,9,2,1,4,7,10]))