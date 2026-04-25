# Enter your code here. Read input from STDIN. Print output to STDOUT

S = list(input())
lchar = [x for x in S if x.islower()]
uchar = [x for x in S if x.isupper()]
odd = [x for x in S if x.isdigit() and (int(x) % 2 != 0)]
even = [x for x in S if x.isdigit() and (int(x) % 2 == 0)]
print(''.join(sorted(lchar) + sorted(uchar) + sorted(odd) + sorted(even)))