cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    seq = [0, 1]
    for _ in range(n-2):
        seq.append(seq[-1]+seq[-2])
    return seq[:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))