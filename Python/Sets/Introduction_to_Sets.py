def average(array):
    unique_height = set(array)
    avg = sum(unique_height)/len(unique_height)
    return avg
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)