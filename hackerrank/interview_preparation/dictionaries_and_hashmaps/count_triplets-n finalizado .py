#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    counter = 0

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] == (arr[i] * r):
                for k in range(j+1, len(arr)):
                    if (arr[j]*r) == arr[k]:
                        counter += 1
    return counter

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    print(ans)
    #fptr.write(str(ans) + '\n')

    #fptr.close()
