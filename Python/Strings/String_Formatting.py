def print_formatted(number):
    max_space = len(bin(number)[2:])
    for i in range(1, number + 1):
        n = str(i).rjust(max_space)
        o = oct(i)[2:].rjust(max_space)
        h = hex(i)[2:].upper().rjust(max_space)
        b = bin(i)[2:].rjust(max_space)
        print(n, o, h, b, sep=' ', end='\n')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)