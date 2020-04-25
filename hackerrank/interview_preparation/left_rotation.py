#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    lefted_array = a.copy()
    for i in range(d):
        temp_array = []
        temp_array.extend(lefted_array[1:])
        temp_array.append(lefted_array[0])

        lefted_array = temp_array
    return lefted_array

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)
    print(result)

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
