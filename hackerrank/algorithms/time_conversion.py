#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    horario = s[:-2]
    indicator = s[-2:]
    result = ''
    part = horario.split(':')
    if indicator == 'AM':
        if part[0] == '12':
            part[0] = '00'
            result = ':'.join(part)
        else:
            result = horario
    else:
        if part[0] != '12':
            hour = int(part[0]) + 12
            part[0] = str(hour)
        result = ':'.join(part)
    return result
        

if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)
    #f.write(result + '\n')

    #f.close()
