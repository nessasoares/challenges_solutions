import pytest

class Array():
    
    def __init__(self, list):
        self.list = list

    def invert(self):
        reverted = reversed(self.list)
        return list(reverted)

class TestArray():
    def test_array(self):
        array = Array([1,4,3,2])

        assert [2,3,4,1] == array.invert()
