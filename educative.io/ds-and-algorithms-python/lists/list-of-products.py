def find_product(arr):
    product = 1

    result = []
    for element in arr:
        product *= element
    
    for index, element in enumerate(arr):
        if element == 0:
            result.append(product)    
        else:
            result.append(product // element)

    return result

print(find_product([1,2,3,4]))
print(find_product([4,2,1,5,0]))