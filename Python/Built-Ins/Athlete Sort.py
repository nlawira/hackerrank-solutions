#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n, m = map(int, input().split())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    k = int(input())
    
    arr = sorted(arr, key = lambda x:x[k])
    
    for data in arr:
        print(' '.join(map(str, data)))    
