def find_first_unique(lst):
    numbers = {}

    for element in lst:
        if element in numbers.keys():
            numbers[element] += 1
        else:
            numbers[element] = 1

    result = 0
    for key, value in numbers.items():
        if value == 1:
            result = key
            break

    return result

lst = [9,2,3,2,6,6]
print(find_first_unique(lst))