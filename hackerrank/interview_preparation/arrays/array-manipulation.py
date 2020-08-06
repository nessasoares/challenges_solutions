import pytest

def arrayManipulation(n, queries):
    array = [0] * (n+1)
    max_value = 0

    for operation in queries:
        first_index, last_index, operation_value = operation;

        array[first_index-1] += operation_value
        array[last_index] -= operation_value

    print(array)
    counter = 0
    for element in array:    
        counter += element
        if counter > max_value:
            max_value = counter

    return max_value

class Test_ArrayManipulation():
    def test_example(self):
        n = 5
        queries = [[1,2,100],
               [2,5,100],
               [3,4,100] 
            ]

        assert 200 == arrayManipulation(n, queries)

        n = 10
        queries = [[1,5,3],
               [4,8,7],
               [6,9,1] 
            ]

        assert 10 == arrayManipulation(n, queries)

        n = 10
        queries = [[2,6,8],
               [3,5,7],
               [1,8,1],
               [5,9,15] 
            ]

        assert 31 == arrayManipulation(n, queries)