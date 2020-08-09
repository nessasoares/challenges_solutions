def find_first_missing_positive(nums):
    duplicated = []
    index = 0
    while index < len(nums):
        target = nums[index] - 2

        if nums[index] != nums[target]:
            nums[index], nums[target] = nums[target], nums[index]
        else:
            if index != target:
                duplicated.append(nums[index])
            index +=1
    return duplicated

# print(find_first_missing_positive([-3, 1, 5, 4, 2]))
# print(find_first_missing_positive([3, -2, 0, 1, 2]))
print(find_first_missing_positive([3, 2, 5, 1]))