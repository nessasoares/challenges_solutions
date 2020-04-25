#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    size = len(grades)
    final_grade = grades.copy()
    for i in range(size):
        if grades[i] < 38:
            final_grade[i] = grades[i]
        else:
            multiple = (grades[i] - (grades[i]%5) + 5)
            if multiple - grades[i] < 3:
                final_grade[i] = multiple
            else:
                final_grade[i] = grades[i]
    return final_grade

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)
    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
