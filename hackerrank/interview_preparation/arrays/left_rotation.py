#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    lefted_array = a.copy()

    first = lefted_array[:d]
    second = lefted_array[d:]
    
    result = second
    result.extend(first)

    return result

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
