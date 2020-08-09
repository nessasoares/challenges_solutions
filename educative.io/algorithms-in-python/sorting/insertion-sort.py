def insertion_sort(lst):

    for atual in range(len(lst)-1):
        if lst[atual] > lst[atual+1]:
            keep_going = True

            i = 1
            
            move_element_index = atual + 1
            move_element = lst[move_element_index]

            move_index = move_element_index
            print(atual, move_index)
            while keep_going:
                if move_index-i >= 0:
                    lst[move_index] = lst[move_index-i]
                    i += 1
                    move_index -= 1

                    if move_element < lst[move_index] and move_element > lst[move_index-i]:
                        lst[move_index] = move_element
                        keep_going = False
            
            print(lst)


print(insertion_sort([5,3,8,6,9,2,1,4,7,10]))