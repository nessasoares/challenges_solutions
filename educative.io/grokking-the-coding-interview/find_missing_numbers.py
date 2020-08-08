def find_missing_numbers(nums):
    nums = cyclic_sort(nums)
    
    missing = []

    for k in range(len(nums)):
        if k + 1 != nums[k]:
            missing.append(k + 1)

    return missing

def cyclic_sort(nums):
    index = 0

    while index < len(nums):
        target = nums[index] - 1
        print(nums)
        if nums[index] != nums[target]:
            nums[index], nums[target] = nums[target], nums[index]
        else:
            index += 1

    return nums

    
print(find_missing_numbers([2,3,1,8,2,3,5,1]))