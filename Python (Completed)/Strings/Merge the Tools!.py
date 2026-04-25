def merge_the_tools(string, k):
    slist = [*string]
    for i in range(0,int(len(slist)/k)):
        bgn = i*k
        end = i*k+k
        temp = slist[bgn:end]
        substring = []
        for x in temp:
            if x not in substring:
                substring.append(x)
        print(''.join(substring))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)