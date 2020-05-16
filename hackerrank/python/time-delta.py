#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime, timezone 

# Complete the time_delta function below.
def time_delta(t1, t2):

    date_1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    date_2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')

    converted_date_1 = date_1.astimezone(tz=timezone.utc)
    converted_date_2 = date_2.astimezone(tz=timezone.utc)

    return (converted_date_1-converted_date_2).total_seconds()

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = int(time_delta(t1, t2))

        print(delta)
        #fptr.write(delta + '\n')

    #fptr.close()
