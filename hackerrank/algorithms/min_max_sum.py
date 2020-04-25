#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    min_list = arr[:4]
    max_list = arr[1:]
    min_sum = sum(min_list)
    max_sum = sum(max_list)
    print('{} {}'.format(str(min_sum), str(max_sum)))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
