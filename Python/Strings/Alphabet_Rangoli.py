alphabet = [chr(i) for i in range(97, 123)]
def print_rangoli(size):
    lsize = size*4-3
    rangoli, l = [], []

    for i in range(size):
        l.append(alphabet[(size-i-1)])
        l2 = l[::-1]
        row = l[:-1] + l2
        row = '-'.join(row)
        row = row.center(lsize, '-')
        rangoli.append(row)
        
    for r in rangoli:
        print(r)
        
    rangoli.pop()
    
    for r in rangoli[::-1]:
        print(r)
            

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)