# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

N = int(input())
word_sequence = list()
for i in range(N):
    line = str(input())
    word_sequence.append(line)
T = int(input())
for i in range(T):
    testcase = str(input())
    total = 0
    for words in word_sequence:
        pattern = testcase[:-2] + "(ze|se)"
        matches = re.findall(pattern, words)
        total += len(matches)
    print(total)