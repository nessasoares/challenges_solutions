#!/bin/python3

import math
import os
import random
import re
import sys

def left_rotation(d, a):
    rotated = a[0:d]
    new_array = a[d:]
    new_array.extend(rotated)

    return new_array

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    result = left_rotation(d,a)
    print(*result)