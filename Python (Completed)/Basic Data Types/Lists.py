if __name__ == '__main__':
    N = int(input())
    sol_list = list()
    for _ in range(N):
        command = input()
        if "insert" in command:
            e = command.split(" ")[2]
            i = command.split(" ")[1]
            sol_list.insert(int(i), int(e))
        elif "print" in command:
            print(sol_list)
        elif "remove" in command:
            e = command.split(" ")[1]
            sol_list.remove(int(e))
        elif "append" in command:
            e = command.split(" ")[1]
            sol_list.append(int(e))
        elif "sort" in command:
            sol_list.sort()
        elif "pop" in command:
            sol_list.pop()
        elif "reverse" in command:
            sol_list.reverse()
        else:
            pass