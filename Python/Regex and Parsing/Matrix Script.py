#!/bin/python3

import math
import os
import random
import re
import sys

def clean_matrix(rows, cols, matrix):
    columns_text = []
    for col in range(cols):
        columns_text.append(''.join(matrix[row][col] for row in range(rows)))
    merged_text = ''.join(columns_text)
    print(re.sub(r'(?<=[\w\d])[^\w\d]+(?=[\d\w])',' ', merged_text))

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

clean_matrix(len(matrix),len(matrix[0]),matrix)