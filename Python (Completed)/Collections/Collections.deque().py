# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

d = deque()
N = int(input())
for _ in range(N):
    command = input().split()
    if len(command) > 1:
        number = int(command[1])
        command = command[0]
    else:
        command = command[0]
    if command == 'append':
        d.append(number)
    elif command == 'appendleft':
        d.appendleft(number)
    elif command == 'pop':
        d.pop()
    elif command == 'popleft':
        d.popleft()
    else:
        pass
print(' '.join(list(map(str, d))))