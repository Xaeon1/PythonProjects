#!/bin/python3

import math
import os
import random
import re
import sys


def plus_minus(arr):
    positive, negative, zeros = 0, 0, 0
    length = len(arr)
    for el in range(length):
        if arr[el] > 0:
            positive += 1
        elif arr[el] < 0:
            negative += 1
        else:
            zeros += 1

    print(round(positive / length, 6))
    print(round(negative / length, 6))
    print(round(zeros / length, 6))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plus_minus(arr)