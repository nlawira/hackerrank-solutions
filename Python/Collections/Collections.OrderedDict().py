# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

N = int(input())
inventory = OrderedDict()
for _ in range(N):
    item, price = input().rsplit(" ", 1)
    inventory[item] = inventory.get(item, 0) + int(price)
for i,j in inventory.items():
    print(i,j)