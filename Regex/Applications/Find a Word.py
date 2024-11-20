# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

sentences = []
N = int(input())
for _ in range(N):
    sentences.append(str(input()))
T = int(input())
for _ in range(T):
    total = 0
    word = str(input())
    pattern = r'(?:(?<=\b)|(?<=\W))'+word+r'(?=\b|\W)'
    for sentence in sentences:
        wfound = re.findall(pattern, sentence)
        total += len(wfound)
    print(total)