import pytest 

def is_permutation(A):
    result = 0
    sorted_array = list(set(A))
    if len(A) == 1:
        result = 0
    difference = sorted_array[-1] - sorted_array[0]
    if difference == len(sorted_array)-1:
        result = 1

    return result


class Test_PermCheck():

    def test_examples(self):
        array = [4,1,3,2]
        assert 1 == is_permutation(array)

        array = [4,1,3]
        assert 0 == is_permutation(array)

    def test_single_element_array(self):

        assert 0 == is_permutation([1])

    
    def test_reapeated_elements(self):
        array = [1,2,2,3,4]
        assert 1 == is_permutation(array)

        array = [1,2,2,5,6,4,7,8,9,12,20]
        assert 0 == is_permutation(array)
