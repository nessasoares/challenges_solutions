#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    key = 'a'
    counter = 0
    new_str = []
    count_key = s.count(key)
    if count_key == len(s):
        return n
    if key in s:
        how_many_keys = s.count(key)
        n_strings = n//len(s)
        miss = n % len(s)
        subs = 0
        if miss > 0:
            subs = s[:miss].count(key)
        counter = (how_many_keys * n_strings) + subs
    return counter

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
