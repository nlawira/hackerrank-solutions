#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = list(input())
    counts = {}
    for i in s:
        counts[i] = counts.get(i,0) + 1
    counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for key, value in counts[:3]:
        print(key, value)