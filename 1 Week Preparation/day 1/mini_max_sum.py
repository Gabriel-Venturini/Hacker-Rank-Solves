#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr = sorted(arr) # sort array from lowest to biggest
    biggest = sum(arr) # sum all elements
    lowest = biggest - arr[-1] # take the last element off
    biggest -= arr[0] # take the first element off

    print(f'{lowest} {biggest}')


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr) # [1, 2, 3, 4, 5]
