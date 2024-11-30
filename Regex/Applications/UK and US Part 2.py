# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

sentences = ''
N = int(input())
for _ in range(N):
    sentences += input() + ' '
    
for _ in range(int(input())):
    uk = input()
    us = uk.replace('our', 'or')
    pattern = r'\b({}|{})\b'.format(uk,us)
    print(len(re.findall(pattern, sentences)))