import pytest 

def count_valleys(s, n):
    level = 0
    last_level = 0
    valley = 0

    for step in s:
        if step == 'D':
            level = level - 1
        elif step == 'U':
            level = level + 1

        print(level)
        if level == 0 and last_level < 0:
            valley += 1

        last_level = level 
    
    return valley


class Test_Counting_Valleys():
    def test_examples(self):
        array = 'UDDDUDUU'
        n = 8

        assert 1 == count_valleys(array, n)