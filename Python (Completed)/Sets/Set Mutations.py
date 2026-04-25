len_a = int(input())
a = set(input().split(" "))
num_sets = int(input())
for _ in range(num_sets):
    operation_len = input()
    operation = operation_len.split(" ")[0]
    len_set = int(operation_len.split(" ")[1])
    operation_set = input().split(" ")
    if operation == "update":
        a.update(operation_set)
    elif operation == "intersection_update":
        a.intersection_update(operation_set)
    elif operation == "difference_update":
        a.difference_update(operation_set)
    else:
        a.symmetric_difference_update(operation_set)
sum_a=0
for x in a:
    sum_a += int(x)
print(sum_a)