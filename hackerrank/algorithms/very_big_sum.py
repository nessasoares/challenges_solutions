#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def aVeryBigSum(ar):
    size = len(ar)
    value = 0
    for i in range(size):
        value += ar[i]
    print(value)
    return value

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    #fptr.write(str(result) + '\n')

    #fptr.close()
