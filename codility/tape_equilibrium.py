import pytest

class Tape():
    
    def __init__(self, tape_content):
        self.content = tape_content

    def minimum_equilibrium(self):
        size = len(self.content)
        minimum_value = float('inf')
        for p in range(1, size):
            first_part = sum(self.content[:p])
            second_part = sum(self.content[p:])

            difference = abs(first_part - second_part)
            
            minimum_value = difference if difference < minimum_value else minimum_value

        return minimum_value


class Test_Tape():
    def test_example(self):
        tape = Tape([3,1,2,4,3])
        
        assert 1 == tape.minimum_equilibrium()
