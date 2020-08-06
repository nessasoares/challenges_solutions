#!/bin/python3

import pytest

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    position = 0
    total_clouds = len(c)

    while position != total_clouds-1:
        did_jump = False
        next_jump = position + 2
        if check_cloud(c, next_jump):
            position = next_jump
            jumps += 1
            did_jump = True


        if not did_jump:
            next_jump = position + 1
            if check_cloud(c, next_jump):
                position = next_jump
                jumps += 1

    return jumps

def check_cloud(array, position):
    if position <= len(array)-1 and array[position] != 1:
        return True
    return False

class Test_Jumping_Cloud():
    def test_example(self):
        c = [0,0,0,0,1,0]
        assert 3 == jumpingOnClouds(c)

        c = [0,0,1,0,0,1,0]
        assert 4 == jumpingOnClouds(c)

        c = [0,1,0,0,0,1,0]
        assert 3 == jumpingOnClouds(c)