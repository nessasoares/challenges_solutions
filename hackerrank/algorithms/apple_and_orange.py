#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    #compare apples
    how_many_apples = 0
    how_many_oranges = 0
    a_array = []
    #import ipdb; ipdb.set_trace()
    for i in range(len(apples)):
        where_fall = a + apples[i]
        if t >= where_fall >= s:
            how_many_apples +=1

    for i in range(len(oranges)):
        where_fall = b + oranges[i]
        if t >= where_fall >= s:
            how_many_oranges +=1
    
    print(how_many_apples)
    print(how_many_oranges)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
