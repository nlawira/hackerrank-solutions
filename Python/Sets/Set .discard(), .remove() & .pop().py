n = int(input())
s = set(map(int, input().split()))
n_commands = int(input())
for _ in range(n_commands):
    command_val = str(input())
    try:
        command = command_val.split(" ")[0]
        val = int(command_val.split(" ")[1])
    except:
        pass
    if command == 'remove':
        try:
            s.remove(val)
        except:
            pass
    elif command == 'discard':
        s.discard(val)
    else:
        s.pop()
print(sum(s))