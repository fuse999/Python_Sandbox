#!/bin/python3
## https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(i, j, arr):
    # get sum for hourglass which top left corner is at i, j
    cur_sum = 0
    cur_sum += sum(arr[i][j:j+3])
    cur_sum += arr[i+1][j+1]
    cur_sum += sum(arr[i+2][j:j+3])
    return cur_sum

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = max([hourglassSum(i, j, arr) for i in range(4) for j in range(4)])

    fptr.write(str(result) + '\n')

    fptr.close()
