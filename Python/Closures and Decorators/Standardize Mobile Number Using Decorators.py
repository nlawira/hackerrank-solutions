def wrapper(f):
    def fun(l):
        # complete the function
        l = [number[len(number)-10:] for number in l]
        for number in sorted(l):
            print("+91", number[0:5], number[5:])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


