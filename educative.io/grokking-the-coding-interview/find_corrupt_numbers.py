def find_corrupt_numbers(nums):
    duplicated = -1
    missing = -1

    index = 0
    while index < len(nums):
        target = nums[index] - 1

        if nums[index] != nums[target]:
            nums[index], nums[target] = nums[target], nums[index]

        else:
            if index != target:
                duplicated = nums[index]
            index += 1
    
    for el in range(len(nums)-1):
        if nums[el]-1 != el:
            missing = el + 1
            break

    return duplicated, missing

print(find_corrupt_numbers([3, 1, 2, 5, 2]))
print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))