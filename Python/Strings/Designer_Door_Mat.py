# Enter your code here. Read input from STDIN. Print output to STDOUT
dim = input()
size = [int(x) for x in dim.split(' ')]
n = size[0]
m = size[1]
countup=0
for i in range(1,n+1):
    if i < (n+1)/2:
        mulup=int((m-3-(countup*6))/2)
        print("-"*mulup+"."+"|..|.."*countup+"|."+"-"*mulup)
        countup+=1
    elif i == (n+1)/2:
        print("-"*int(((m-7)/2))+"WELCOME"+"-"*int(((m-7)/2)))
        countdown = countup-1 
    else:
        muldown=int((m-3-(countdown*6))/2)
        print("-"*muldown+"."+"|..|.."*countdown+"|."+"-"*muldown)
        countdown-=1