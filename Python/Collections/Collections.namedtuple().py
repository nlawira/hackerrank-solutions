# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n, student_info, students, total = int(input()), namedtuple('student_info', input().split()), [], 0
for i in range(n):
    students.append(student_info(*input().split()))
    total += int(students[i].MARKS)

print(total/n)
