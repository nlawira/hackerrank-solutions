# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

N = int(input())
letters = input().split()
K = int(input())
chosen = list(itertools.combinations(letters, K))
count = 0
for i in chosen:
    if 'a' in i:
        count += 1
print(round(count/len(chosen), 3))
