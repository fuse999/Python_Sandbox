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


# Complete the twoStrings function below.
# def twoStrings(s1, s2):
#     answer = []
#     for i in range(0, 2):
#         action = False
#         first_str_hash = {}
#         for c in s1[i]:
#             if c in first_str_hash:
#                 first_str_hash[c] += 1
#             else:
#                 first_str_hash[c] = 1
#         for c in s2[i]:
#             if c in first_str_hash and first_str_hash[c] > 0:
#                 first_str_hash[c] -= 1
#                 action = True
#                 break
#             else:
#                 continue
#         if action == False:
#             answer.append("NO")
#         elif action == True:
#             answer.append("YES")
#     return answer


#But too slow
# def twoStrings(s1, s2):
#     for i in range(0,len(s1)):
#         if(s1[i] in s2):
#             return "YES"
#             break
#     else:
#         return "NO"

hello = "hello"
world = "world"

print(twoStrings(hello, world))