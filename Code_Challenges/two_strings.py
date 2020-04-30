import math
import os
import random
import re
import sys

# Final answer
#First implemtation
def twoStrings(s1, s2):
    answer = "NO"
    first_str_hash = {}
    for c in s1:
        if c in first_str_hash:
            first_str_hash[c] += 1
        else:
            first_str_hash[c] = 1
           
    for c in s2:
        if c in first_str_hash and first_str_hash[c] > 0:
            first_str_hash[c] -= 1
            answer = "YES"
            break
        else:
            continue
    print(answer)

hello = "hello"
world = "world"

print(twoStrings(hello, world))