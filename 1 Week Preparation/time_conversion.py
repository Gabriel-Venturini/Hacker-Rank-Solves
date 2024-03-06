#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    newS = ''
    twoFirst = int(s[0:2])
    if 'AM' in s:
        newS = s.replace('12', '00')[0:-2]
    elif 'PM' in s:
        if twoFirst < 12:
            newS= str(twoFirst + 12) + s[2:-2]
        else:
            newS = s[:-2]

    return newS


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
