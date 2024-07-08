if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorted_list = sorted(arr, reverse=True)
    max_number = sorted_list[0]
    x = 1
    while sorted_list[x] == max_number:
        x += 1
    print(sorted_list[x])