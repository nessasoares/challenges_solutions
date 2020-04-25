#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    can = False
    k1 = (x1, v1)
    k2 = (x2, v2)

    min_dist = k1 if x1 < x2 else k2
    max_dist = k1 if x1 > x2 else k2

    if min_dist[1] < max_dist[1]:
        can = False
    elif v1 == v2 and x1 != x2:
        can = False
    else:    
        keep_going = True
        position_1 = x1+v1
        position_2 = x2+v2

        while keep_going:
            if position_1 == position_2:
                keep_going = False
                can = True
                break
            elif abs(position_1 - position_2) > max_dist[0]:
                keep_going = False
                can = False
                break
            else:
                position_1 += v1
                position_2 += v2
                print('{} : {}'.format(str(position_1), str(position_2)))
    
    result = 'YES' if can else 'NO'
    return result


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)
    print(result)

    #fptr.write(result + '\n')

    #fptr.close()
