def find_missing_number(lst):
    lst = sort(lst)
    print(lst)

    for i in range(len(lst)):
        if i != lst[i]:
            return i

def sort(lst):
    '''
    Cyclic sort
    '''
    index = 0

    while index < len(lst):
        target = lst[index]

        if target != index and target < len(lst):
            lst[index], lst[target] = lst[target], lst[index]

        else:
            index += 1
    
    return lst


print(find_missing_number([4,0,3,1]))