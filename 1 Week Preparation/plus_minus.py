#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive, negative, zero = 0, 0, 0
    # Write your code here
    for number in arr:
        if number == 0:
            zero += 1
        elif number > 0:
            positive += 1
        else:
            negative += 1

    print(f'{positive / len(arr)}') # positive
    print(f'{negative / len(arr)}') # negative
    print(f'{zero / len(arr)}') # zero
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)