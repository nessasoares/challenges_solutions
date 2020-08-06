def find_minimum(arr):
    minimum = arr[0]
    for element in arr:
        if element < minimum:
            minimum = element

    return minimum

print(find_minimum([9,15, 6,27,33,6,95,36,32,35,66,369,235,36,59,84,87,65,95,14,36,65,95,9982,3,6]))
