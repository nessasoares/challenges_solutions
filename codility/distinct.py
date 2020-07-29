import pytest

def get_distinct_elements(A):
    set_A = set(A)
    return len(set_A)

class TestDistinct():
    def test_examples(self):
        A = [2,1,1,2,3,1]

        assert 3 == get_distinct_elements(A) 
