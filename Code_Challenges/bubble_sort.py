import math
import os
import random
import re
import sys

a = [6, 4, 1]
# Complete the countSwaps function below.
def countSwaps(a):
    n = len(a) 
    swapcount = 0
    for i in range(n): 
        for j in range(0, n-i-1): 
            if a[j] > a[j+1]:
                swapcount += 1
                a[j], a[j+1] = a[j+1], a[j] 
    print(f"Array is sorted in {swapcount} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

countSwaps(a)
