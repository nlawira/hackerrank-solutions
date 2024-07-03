#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    list_s = s.split(' ')
    new_list = []
    for word in list_s:
        new_list.append(word.capitalize())
    return ' '.join(new_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
