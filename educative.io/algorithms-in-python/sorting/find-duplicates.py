def find_duplicates(array):
    visited = {}
    duplicated = []

    for element in array:
        if element not in visited.keys():
            visited[element] = 1

        else:
            if element not in duplicated:
                duplicated.append(element)
            visited[element]+=1
        
    return duplicated

print(find_duplicates([1, 3, 1, 3, 5, 1, 4, 7, 7]))