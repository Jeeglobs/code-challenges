# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

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
    # Write your code here
    posi = []
    negi = []
    zero = []
    for n in arr:
        if n > 0:
            posi.append(n)
        elif n < 0:
            negi.append(n)
        else:
            zero.append(n)
    posi_ratio = len(posi) / len(arr)
    negi_ratio = len(negi) / len(arr)
    zero_ratio = len(zero) / len(arr)

    print(f"{posi_ratio:.6f}")
    print(f"{negi_ratio:.6f}")
    print(f"{zero_ratio:.6f}")
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
