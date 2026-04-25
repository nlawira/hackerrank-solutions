# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import groupby

S = input()
for i, j in groupby(S):
    print((len(list(j)) ,int(i)), end=" ")
