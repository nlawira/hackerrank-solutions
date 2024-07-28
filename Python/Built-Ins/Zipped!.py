# Enter your code here. Read input from STDIN. Print output to STDOUT

N, X = map(int, input().split())
total = []
for _ in range(X):
    total = total + [map(float, input().split())]
marks = zip(*total)
for mark in marks:
    print("%.1f" % (sum(mark)/len(mark)))