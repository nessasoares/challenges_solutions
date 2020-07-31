def max_counters(N, A):
    array = [0]* N
    max_counters = []
    max_value = 0

    for element in A:
        if element >= 1 and element <= N:
            array[element-1] += 1 
            if array[element-1] > max_value:
                max_value = array[element-1]

        elif element > N:
            array = [max_value] * N

    return array


a = max_counters(5, [3,4,4,6,1,4,4])
print(a)