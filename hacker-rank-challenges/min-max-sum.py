# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

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
    arr.sort()
    min_array = arr[:4]
    max_array = arr[-4:]
    min_sum = 0
    max_sum = 0
    
    for i in min_array:
        min_sum = min_sum + i
    
    for i in max_array:
        max_sum = max_sum + i
    
    print(f"{min_sum} {max_sum}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
