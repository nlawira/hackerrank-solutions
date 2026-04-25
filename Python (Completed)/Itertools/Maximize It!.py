import itertools

ip = list(map(int, input().split()))
num = ip[0]
div = ip[1]

total = 0
numbers = []

for n in range(num):
    numbers.append(list(set(map(int, input().split()[1:]))))

combinations = list(itertools.product(*numbers))

maximum = -1
for combo in combinations:
    total_squares = sum([number ** 2 for number in list(combo)])
    modulo = total_squares % div
    if modulo > maximum:
        maximum = modulo
print(maximum)
