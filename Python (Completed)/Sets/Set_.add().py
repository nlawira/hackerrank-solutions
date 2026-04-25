# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
collection = set()
for _ in range(n):
    stamp = str(input())
    collection.add(stamp)
print(len(collection))