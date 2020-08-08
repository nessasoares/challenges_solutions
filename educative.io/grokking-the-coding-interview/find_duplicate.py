def find_duplicate(nums):

    i = 0
    duplicated = []

    while i < len(nums):
        
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[j] != nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
            else:
                return nums[i]
        else:
            i += 1
    
    return duplicated

def find_all_duplicates(nums):
    i = 0
    duplicated = []

    while i < len(nums):
        j = nums[i] -1

        if nums[j] != nums[i]:
            nums[j], nums[i] = nums[i], nums[j]
        else:
            if i != j:
                duplicated.append(nums[i])
            i += 1

    return duplicated

# print(find_duplicate([3, 4, 4, 5, 5]))
# print(find_duplicate([5, 4, 7, 2, 3, 5, 3]))
# print('--')
print(find_all_duplicates([3, 4, 4, 5, 5]))
print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))