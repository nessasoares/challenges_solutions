#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    size = len(arr)
    first = 0
    second = 0
    f=[]
    s=[]
    for i in range(size):
        for j in range(size): 
            if i == j:
                first += arr[i][j]
                f.append(arr[i][j])
                second += arr[-i-1][j] 
                s.append(arr[-i-1][j])
    print(f)
    print(s)
    print('{} + {}'.format(str(first), str(second)))
    result = abs(first-second)
    print(str(result))
    return result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    #fptr.write(str(result) + '\n')

    #fptr.close()
