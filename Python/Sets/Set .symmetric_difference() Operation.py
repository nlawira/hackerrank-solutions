engno = int(input())
eng = input()
freno = int(input())
fre = input()
a = set(eng.split(' ')).symmetric_difference(fre.split(' '))
print(len(a))