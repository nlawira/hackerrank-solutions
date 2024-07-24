# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())
for _ in range(T):
    a, b = map(str, input().split())
    try:
        print(int(a)//int(b))
    except ValueError as VE:
        print("Error Code:", VE)
    except ZeroDivisionError as ZDE:
        print("Error Code:", ZDE)