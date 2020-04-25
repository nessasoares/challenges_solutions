#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

#    import ipdb; ipdb.set_trace()
    is_odd = n % 2 != 0
    is_in_the_range_2_to_5 = 2 <= n and n <= 5
    is_in_the_range_6_to_20 = 6 <= n <= 20
    is_greater_than_20 = n >= 20

    if is_odd or is_in_the_range_6_to_20:
        print("Weird")
    elif is_in_the_range_2_to_5 or is_greater_than_20:
        print('Not Weird')