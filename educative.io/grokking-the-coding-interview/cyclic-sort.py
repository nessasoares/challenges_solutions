def cyclic_sort(lst):
    i = 0

    while i < len(lst):
        n = lst[i]-1

        if i != n:
            lst[i], lst[n] = lst[n], lst[i]
        else:
            i += 1

    return lst

print(cyclic_sort([5,3,8,6,9,2,1,4,7,10]))