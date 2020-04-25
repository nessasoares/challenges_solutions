#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    checked = set()
    pairs = 0
    for i in range(n):
        if ar[i] not in checked:
            counter = ar.count(ar[i])
            pairs += (counter//2)
            checked.add(ar[i])
    return pairs

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    #fptr.write(str(result) + '\n')

    #fptr.close()
