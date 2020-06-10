#!/bin/python3

import math
import os
import random
import re
import sys


# write your code here
def avg(*nums):
    total_sum = sum(nums)
    average = total_sum/len(nums)
    return float(average)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(*nums)
    print('%.2f' % res + '\n')
    
    #fptr.write('%.2f' % res + '\n')

    #fptr.close()