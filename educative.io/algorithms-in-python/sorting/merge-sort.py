def merge_sort(array):
    
    if len(array) > 1:
        print("i'm in")

        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]

        left = merge_sort(left)
        right = merge_sort(right)

        l = 0
        r = 0
        k = 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                array[k] = left[l]
                l+=1
            else:
                array[k] = right[r]
                r +=1

            k+=1

        while l< len(left):
            array[k] = left[l]
            l +=1
            k += 1

        while r< len(right):
            array[k] = right[r]
            r +=1
            k += 1


    return array

    


print(merge_sort([2,3,0,1,2,56,36,3569,22,14,25,35,36,38,39]))