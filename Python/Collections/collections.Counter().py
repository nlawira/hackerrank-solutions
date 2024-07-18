# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

X = int(input())
shoe_size = Counter(input().split(" "))
N = int(input())
total = 0
for _ in range(N):
    size, price = input().split(" ")
    if size not in shoe_size.keys():
        continue
    elif shoe_size[size] != 0:
        total += int(price)
        shoe_size[size] -= 1
    else:
        continue
print(total)