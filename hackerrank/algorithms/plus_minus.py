#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    size = len(arr)
    zeros = 0
    positives = 0
    negatives = 0

    for i in range(size):
        if arr[i]==0:
            zeros +=1
        elif arr[i] > 0:
            positives += 1
        elif arr[i] < 0:
            negatives += 1
    
    print(positives/size)
    print(negatives/size)
    print(zeros/size)
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
