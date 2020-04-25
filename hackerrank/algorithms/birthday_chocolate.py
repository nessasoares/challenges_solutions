#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below
def birthday(s, d, m):
    subarrays = [s[i:i+m] for i in range(len(s)) if len(s[i:i+m]) == m]
    options = 0
    for sub in subarrays:
        if sum(sub) == d:
            options += 1
    return options
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    #fptr.write(str(result) + '\n')

    #fptr.close()
