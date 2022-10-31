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
    min_sum = 0
    max_sum = 0
    length = len(arr)

    arr.sort()
    j = length - 1
    for el in range(length - 1):
        min_sum += arr[el]

        max_sum += arr[j]
        j -= 1

    print(min_sum, max_sum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
